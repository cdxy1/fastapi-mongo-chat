from beanie.operators import All

from backend.model.room import RoomModel
from backend.model.user import UserModel


class RoomRepository:
    @staticmethod
    async def create(name: str, participants: list[UserModel]) -> RoomModel:
        room = await RoomModel(name=name, participants=participants).insert()

        return room

    @staticmethod
    async def find_by_name(name: str) -> RoomModel:
        room = await RoomModel.find_one({"name": name})

        return room

    @staticmethod
    async def find_with_participant(name: str) -> RoomModel:
        rooms = RoomModel.find_many(
            RoomModel.participants.username == name, fetch_links=True
        )

        return await rooms.to_list()

    @staticmethod
    async def find_with_participants(names: list[str]) -> RoomModel:
        rooms = RoomModel.find_many(
            All(RoomModel.participants.username, names), fetch_links=True
        )

        return await rooms.to_list()
