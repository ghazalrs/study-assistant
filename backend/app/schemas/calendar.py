from pydantic import BaseModel
from datetime import datetime

class CalendarEvent(BaseModel):
    title: str
    start: datetime
    end: datetime

class CalendarPreviewRequest(BaseModel):
    course_id: int

# What the API returns when it parses the syllabus. 
# The user can review and edit before anything gets added to Google Calendar.
class CalendarPreviewResponse(BaseModel):
    events: list[CalendarEvent]

class CalendarCommitRequest(BaseModel):
    events: list[CalendarEvent]