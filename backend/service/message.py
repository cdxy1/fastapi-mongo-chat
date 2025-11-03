from backend.models.room import RoomModel
from backend.models.user import UserModel
from backend.repo.message import MessageRepo


class MessageService:
    @staticmethod
    async def create_message(content: str, sender: UserModel, room: RoomModel):
        await MessageRepo.create(content, sender, room)
