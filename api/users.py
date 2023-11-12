import fastapi
from fastapi import Path


router = fastapi.APIRouter()


@router.get("/user", tags=["Get"])
async def get_user():
    return {"message":"All done!"}


@router.post("/user", tags=["Post"])
async def create_user():
    return {"message":"All done!"}


@router.get("/users/{id}", tags=["Get"])
async def get_user_by_id(
    id: int = Path(..., description="The ID of the user you want to retrieve")
):
    return {}