from pydantic import BaseModel

class EmailDraftRequest(BaseModel):
    course_id: int
    intent: str

class EmailDraftResponse(BaseModel):
    draft_id: str
    to: str
    subject: str
    body: str

class EmailSendRequest(BaseModel):
    draft_id: str