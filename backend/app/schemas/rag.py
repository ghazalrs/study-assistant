from pydantic import BaseModel

class RAGQuery(BaseModel):
    course_id: int
    question: str

class Citation(BaseModel):
    file: str
    page: int
    chunk_id: str

class RAGResponse(BaseModel):
    answer: str
    citations: list[Citation]