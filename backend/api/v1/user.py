from fastapi import APIRouter

from backend.dao.user_dao import UserDAO

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users():
    users = await UserDAO().read_all()
    return users
