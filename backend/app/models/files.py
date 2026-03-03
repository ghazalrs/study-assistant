from sqlmodel import Field, SQLModel
from datetime import datetime


class File(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course_id: int = Field(foreign_key="course.course_id", index=True)
    user_id: int = Field(foreign_key="user.user_id", index=True)
    filename: str
    file_type: str  # "syllabus" or "notes"
    s3_key: str     
    created_at: datetime = Field(default_factory=datetime.utcnow)
