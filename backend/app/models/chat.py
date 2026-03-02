from sqlmodel import Field, SQLModel
from datetime import datetime


class ChatSession(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course_id: int = Field(foreign_key="course.course_id", index=True)
    user_id: int = Field(foreign_key="user.user_id", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="chatsession.id", index=True)
    role: str  # "user" or "assistant"
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
