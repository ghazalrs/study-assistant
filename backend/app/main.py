from fastapi import FastAPI
from .routers import courses
from .routers import files
from .routers import rag
from .routers import email
from .routers import calendar

app = FastAPI()

app.include_router(courses.router)
app.include_router(files.router)
app.include_router(rag.router)
app.include_router(email.router)
app.include_router(calendar.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}