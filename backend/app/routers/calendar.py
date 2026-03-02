from fastapi import APIRouter
from ..schemas.calendar import CalendarEvent, CalendarPreviewRequest, CalendarPreviewResponse, CalendarCommitRequest

router = APIRouter()


@router.post("/calendar/preview")
async def preview(course_id: CalendarPreviewRequest) -> CalendarPreviewResponse:
    pass


@router.post("/calendar/commit")
async def commit(request: CalendarCommitRequest) -> list[CalendarEvent]:
    pass
