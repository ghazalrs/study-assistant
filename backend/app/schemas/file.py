from pydantic import BaseModel

class PresignRequest(BaseModel):
    filename: str
    file_type: str # "syllabus" or "notes"

class PresignResponse(BaseModel):
    upload_url: str
    s3_key: str

class FileCompleteRequest(BaseModel):
    s3_key: str
    filename: str
    file_type: str