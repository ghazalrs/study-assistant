from ..schemas.email import EmailDraftRequest, EmailDraftResponse, EmailSendRequest
from fastapi import APIRouter

router = APIRouter()


@router.post("/email/draft")
async def create_draft(request: EmailDraftRequest) -> EmailDraftResponse:
    pass


@router.post("/email/send")
async def send_email(draft: EmailSendRequest):
    pass
