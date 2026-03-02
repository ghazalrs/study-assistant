from fastapi import APIRouter
from ..schemas.course import CourseCreate, CourseRead

router = APIRouter()


@router.get("/courses")
async def get_course() -> list[CourseRead]:
    pass


@router.post("/courses")
async def create_course(course: CourseCreate) -> CourseRead:
    pass

@router.delete("/courses/{id}")
async def delete_course(id: int):
    pass