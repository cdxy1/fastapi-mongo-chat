from beanie import Link

from backend.models.chat import ChatRoomModel
from backend.models.user import UserModel


class RoomRepo:
    @staticmethod
    async def create(name: str, participants: list[UserModel]):
        await ChatRoomModel(
            name=name, participants=[Link(participant) for participant in participants]
        ).insert()
