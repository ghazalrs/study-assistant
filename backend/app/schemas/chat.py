from pydantic import BaseModel

class Query(BaseModel):
    question: str

class Citation(BaseModel):
    file: str
    page: int
    chunk_id: str

class Response(BaseModel):
    answer: str
    citations: list[Citation]