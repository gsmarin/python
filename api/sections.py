import fastapi
from fastapi import Path


router = fastapi.APIRouter()


@router.get("/sections", tags=["Get"])
async def get_sections():
    return {"message":"All done!"}


@router.post("/sections", tags=["Post"])
async def create_sections():
    return {"message":"All done!"}


@router.get("/sections/{id}", tags=["Get"])
async def get__sections_by_id(
    id: int = Path(..., description="The ID of the user you want to retrieve")
):
    return {}