from beanie import Link

from backend.models.chat import ChatRoomModel
from backend.models.message import MessageModel
from backend.models.user import UserModel


class MessageRepo:
    @staticmethod
    async def create(content: str, sender: UserModel, room: ChatRoomModel):
        new_msg = MessageModel(content=content, sender=Link(sender), room=Link(room))
        await new_msg.insert()

    @staticmethod
    async def find_by_chat_id(room: str):
        messages = await MessageModel.find_all(ChatRoomModel.name == room).to_list()

        return messages
