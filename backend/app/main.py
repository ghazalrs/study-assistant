from fastapi import FastAPI
from sqlmodel import SQLModel
from .routers import auth, chat, courses, files, email, calendar
from .database import engine

app = FastAPI()

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(files.router)
app.include_router(chat.router)
app.include_router(email.router)
app.include_router(calendar.router)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
