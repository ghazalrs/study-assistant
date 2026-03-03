from fastapi import APIRouter
from ..schemas.rag import RAGQuery, RAGResponse

router = APIRouter()


@router.post("/chat/{course_id}")
async def query(course_id: int, request: RAGQuery) -> RAGResponse:
    pass


