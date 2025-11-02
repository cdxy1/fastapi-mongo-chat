from backend.models.chat import ChatRoomModel
from backend.models.user import UserModel


class RoomRepo:
    @staticmethod
    async def create(name: str, participants: list[UserModel]):
        room = await ChatRoomModel(name=name, participants=participants).insert()

        return room
