from sqlmodel import Field, SQLModel
from datetime import datetime


class CalendarEvent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course_id: int = Field(foreign_key="course.course_id", index=True)
    user_id: int = Field(foreign_key="user.user_id", index=True)
    title: str
    start: datetime
    end: datetime
    google_event_id: str | None = None  
    status: str = "pending"  # "pending", "created", "deleted"
    created_at: datetime = Field(default_factory=datetime.utcnow)
