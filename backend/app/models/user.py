from sqlmodel import Field, SQLModel
from datetime import datetime


class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str
    hashed_password: str | None = None
    google_id: str | None = Field(default=None, unique=True, index=True)
    avatar_url: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
