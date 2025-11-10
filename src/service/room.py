from uuid import uuid4

from src.model.room import RoomModel
from src.model.user import UserModel
from src.repository.room import RoomRepository


class RoomService:
    @staticmethod
    async def create_p2p_room(recipients: list[UserModel]) -> RoomModel:
        room_name = str(uuid4())

        room = await RoomRepository.create(room_name, recipients)

        return room

    @staticmethod
    async def get_room(name: str) -> RoomModel:
        room = await RoomRepository.find_by_name(name)

        return room

    @staticmethod
    async def get_room_users(name: str) -> list[UserModel]:
        room = await RoomModel.find_one({"name": name}, fetch_links=True)
        if not room:
            return []
        room_users = room.participants
        return room_users

    @staticmethod
    async def get_or_create_p2p_room(
        sender: UserModel, receiver: UserModel
    ) -> RoomModel:
        rooms = await RoomRepository.find_with_participants(
            [receiver.username, sender.username]
        )

        for room in rooms:
            if len(room.participants) == 2:
                return room

        room = await RoomService.create_p2p_room([sender, receiver])
        return room
