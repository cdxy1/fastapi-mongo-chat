from uuid import uuid4

from backend.models.room import RoomModel
from backend.models.user import UserModel
from backend.repo.room import RoomRepo


class RoomService:
    async def create_p2p_room(sender: UserModel, recepient: UserModel) -> RoomModel:
        room_name = str(uuid4())

        room = await RoomRepo.create(room_name, [sender, recepient])

        return room

    async def create_group_room(): ...

    async def get_room(name: str) -> RoomModel:
        room = await RoomRepo.get_by_name(name)

        return room
