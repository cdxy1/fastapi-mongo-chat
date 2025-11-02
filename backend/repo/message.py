from backend.models.message import MessageModel
from backend.models.room import RoomModel
from backend.models.user import UserModel


class MessageRepo:
    @staticmethod
    async def create(content: str, sender: UserModel, room: RoomModel):
        new_msg = MessageModel(content=content, sender=sender, room=room)
        await new_msg.insert()

    @staticmethod
    async def find_by_room_id(room: str):
        messages = await MessageModel.find_all(RoomModel.name == room).to_list()

        return messages
