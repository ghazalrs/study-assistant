from fastapi import APIRouter
from ..schemas.rag import RAGQuery, RAGResponse

router = APIRouter()


@router.post("/rag/query")
async def query(request: RAGQuery) -> RAGResponse:
    pass


