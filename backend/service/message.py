from backend.model.room import RoomModel
from backend.model.user import UserModel
from backend.repository.message import MessageRepository


class MessageService:
    @staticmethod
    async def create_message(content: str, sender: UserModel, room: RoomModel):
        await MessageRepository.create(content, sender, room)
