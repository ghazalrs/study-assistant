from fastapi import APIRouter
from ..schemas.chat import Query, Response, Citation
from ..rag import query_rag

router = APIRouter()


@router.post("/chat/{course_id}")
async def query(request: Query, course_id: int) -> Response:
    result = query_rag(request.question, course_id)
    return Response(answer=result["answer"], citations=result["citations"])



