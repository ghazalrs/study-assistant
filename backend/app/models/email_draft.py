from sqlmodel import Field, SQLModel
from datetime import datetime


class EmailDraft(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course_id: int = Field(foreign_key="course.course_id", index=True)
    user_id: int = Field(foreign_key="user.user_id", index=True)
    gmail_draft_id: str | None = None  
    to: str
    subject: str
    body: str
    status: str = "draft"  # "draft" or "sent"
    created_at: datetime = Field(default_factory=datetime.utcnow)
