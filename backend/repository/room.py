from backend.models.room import RoomModel
from backend.models.user import UserModel


class RoomRepo:
    @staticmethod
    async def create(name: str, participants: list[UserModel]) -> RoomModel:
        room = await RoomModel(name=name, participants=participants).insert()

        return room

    @staticmethod
    async def get_by_name(name: str) -> RoomModel:
        room = await RoomModel.find_one({"name": name})

        return room

    @staticmethod
    async def get_by_user(name: str) -> RoomModel:
        rooms = RoomModel.find_many({"participants.username": name}, fetch_links=True)

        return await rooms.to_list()
