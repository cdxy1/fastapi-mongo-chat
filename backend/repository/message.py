from backend.model.message import MessageModel
from backend.model.room import RoomModel
from backend.model.user import UserModel


class MessageRepository:
    @staticmethod
    async def create(content: str, sender: UserModel, room: RoomModel):
        msg = MessageModel(content=content, sender=sender, room=room)
        await msg.insert()

        return msg

    @staticmethod
    async def find_by_room_id(room: str):
        messages = await MessageModel.find_all(RoomModel.name == room).to_list()

        return messages
