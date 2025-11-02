from fastapi import APIRouter

from backend.repo.user import UserRepo

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users():
    users = await UserRepo().find_all()
    return users
