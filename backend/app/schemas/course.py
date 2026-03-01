from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str

class CourseRead(BaseModel):
    course_id: int
    title: str
    model_config = {"from_attributes": True}