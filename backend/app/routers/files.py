from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.database import SessionDep
from ..schemas.file import PresignRequest, PresignResponse, FileCompleteRequest
from ..models.file import File

router = APIRouter()


@router.get("/courses/{course_id}/files")
async def get_files(course_id: int, session: SessionDep):
    files = session.exec(select(File).where(File.course_id == course_id)).all()
    return files


@router.delete("/courses/{course_id}/files/{file_id}")
async def delete_file(course_id: int, file_id: int, session: SessionDep):
    file = session.get(File, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    if file.course_id != course_id:
        raise HTTPException(status_code=403, detail="File does not belong to this course")
    session.delete(file)
    session.commit()
    return {"ok": True}


@router.post("/courses/{course_id}/file/presign")
async def upload_file(session: SessionDep):
    pass


@router.post("/courses/{course_id}/file/complete")
async def upload_file(session: SessionDep):
    pass
 