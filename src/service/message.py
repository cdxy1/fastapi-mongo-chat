from src.model.room import RoomModel
from src.model.user import UserModel
from src.repository.message import MessageRepository


class MessageService:
    @staticmethod
    async def create_message(content: str, sender: UserModel, room: RoomModel):
        await MessageRepository.create(content, sender, room)
