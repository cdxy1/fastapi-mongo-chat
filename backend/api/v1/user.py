from fastapi import APIRouter

from backend.repository.room import RoomRepo

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users(): ...


@router.get("/kek")
async def kek():
    a = await RoomRepo.find_with_participants(["jojo1", "jojo2"])
    return a
