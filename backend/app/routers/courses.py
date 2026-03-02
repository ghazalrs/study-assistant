from fastapi import APIRouter, HTTPException
from sqlmodel import select
from ..schemas.course import CourseCreate, CourseRead
from ..models.course import Course
from app.database import SessionDep

router = APIRouter()


@router.get("/courses")
async def get_course(session: SessionDep) -> list[CourseRead]:
    courses = session.exec(select(Course)).all()
    return courses

@router.post("/courses")
async def create_course(course: CourseCreate, session: SessionDep) -> CourseRead:
    db_course = Course.model_validate(course)
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course

@router.delete("/courses/{course_id}")
async def delete_course(course_id: int, session: SessionDep):
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    session.delete(course)
    session.commit()
    return {"ok": True}