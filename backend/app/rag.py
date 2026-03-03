import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

_DB_URL = os.environ["DATABASE_URL"].replace(
    "postgresql://", "postgresql+psycopg://"
)

_embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

_SYSTEM_PROMPT = """You are a study assistant. Answer questions strictly based on the provided course documents.
Rules:
- Never claim facts not present in the provided context.
- Always cite your sources using the format [file: <filename>, page: <page>].
- If the context does not contain enough information, say: "I don't have enough information in the uploaded materials to answer this."
"""

_PROMPT = ChatPromptTemplate.from_messages([
    ("system", _SYSTEM_PROMPT),
    ("human", "CONTEXT:\n{context}\n\nQUESTION:\n{question}\n\nAnswer using only the context above. Include citations."),
])


def _get_vector_store(course_id: int) -> PGVector:
    return PGVector(
        embeddings=_embeddings,
        collection_name=f"course_{course_id}",
        connection=_DB_URL,
    )


def ingest_document(file_path: str, metadata: dict) -> int:
    """Load a PDF, split into chunks, embed, and store in PGVector. Returns chunk count."""
    docs = PyPDFLoader(file_path).load()
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    ).split_documents(docs)

    for chunk in chunks:
        chunk.metadata.update(metadata)

    _get_vector_store(metadata["course_id"]).add_documents(chunks)
    return len(chunks)


def query_rag(question: str, course_id: int) -> dict:
    """Retrieve relevant chunks and generate an answer with citations."""
    docs = _get_vector_store(course_id).similarity_search(question, k=5)

    if not docs:
        return {
            "answer": "I don't have enough information in the uploaded materials to answer this.",
            "citations": [],
        }

    context = "\n\n---\n\n".join(
        f"[file: {d.metadata.get('source', 'unknown')}, page: {d.metadata.get('page', '?')}]\n{d.page_content}"
        for d in docs
    )

    llm = ChatOpenAI(model="gpt-4o-mini")
    response = (_PROMPT | llm).invoke({"context": context, "question": question})

    seen = set()
    citations = []
    for d in docs:
        key = (d.metadata.get("source", ""), d.metadata.get("page", 0))
        if key not in seen:
            seen.add(key)
            citations.append({
                "file": d.metadata.get("source", "unknown"),
                "page": d.metadata.get("page", 0),
                "chunk_id": str(d.metadata.get("id", "")),
            })

    return {"answer": response.content, "citations": citations}
