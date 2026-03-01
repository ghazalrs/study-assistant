from fastapi import APIRouter

router = APIRouter()


@router.get("/courses/", tags=["courses"])
async def get_courses():
    pass


@router.post("/courses/", tags=["courses"])
async def create_course():
    pass
