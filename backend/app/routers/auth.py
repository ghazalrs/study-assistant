from fastapi import APIRouter, HTTPException
from sqlmodel import select
from passlib.context import CryptContext
from ..schemas.auth import LoginRequest

from ..models.user import User
from ..database import SessionDep

router = APIRouter(prefix="/auth")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/login")
def login(body: LoginRequest, session: SessionDep):
    user = session.exec(select(User).where(User.email == body.email)).first()
    if not user or not user.hashed_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not pwd_context.verify(body.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"id": str(user.user_id), "name": user.name, "email": user.email}
