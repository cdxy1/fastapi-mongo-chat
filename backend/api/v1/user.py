from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users(): ...
