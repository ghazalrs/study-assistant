from sqlmodel import Field, SQLModel
from datetime import datetime


class Chunk(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    file_id: int = Field(foreign_key="file.id", index=True)
    course_id: int = Field(foreign_key="course.course_id", index=True)
    user_id: int = Field(foreign_key="user.user_id", index=True)
    page: int
    chunk_index: int
    text: str
    # embedding vector added here after pgvector is installed
    created_at: datetime = Field(default_factory=datetime.utcnow)
