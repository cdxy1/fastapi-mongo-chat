from backend.models.room import RoomModel
from backend.models.user import UserModel


class RoomRepo:
    @staticmethod
    async def create(name: str, participants: list[UserModel]):
        room = await RoomModel(name=name, participants=participants).insert()

        return room
