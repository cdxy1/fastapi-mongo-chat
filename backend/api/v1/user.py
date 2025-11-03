from fastapi import APIRouter

from backend.repository.user import UserRepo

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users():
    users = await UserRepo().find_all()
    return users


@router.get("/kek")
async def kek():
    from backend.repository.room import RoomRepo

    a = await RoomRepo.get_by_user("jojo1")
    return a
