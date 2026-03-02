from sqlmodel import Field, SQLModel
from datetime import datetime


class Course(SQLModel, table=True):
    course_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id", index=True)
    title: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
