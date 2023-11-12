import fastapi
from fastapi import Path


router = fastapi.APIRouter()


@router.get("/courses", tags=["Get"])
async def get_courses():
    return {"message":"All done!"}


@router.post("/courses", tags=["Post"])
async def create_courses():
    return {"message":"All done!"}


@router.get("/courses/{id}", tags=["Get"])
async def get_courses_by_id(
    id: int = Path(..., description="The ID of the user you want to retrieve")
):
    return {}