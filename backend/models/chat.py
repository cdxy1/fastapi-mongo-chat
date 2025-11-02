from beanie import Document, Link

from backend.models.message import MessageModel
from backend.models.user import UserModel


class ChatRoomModel(Document):
    participants: list[Link[UserModel]]
    messages: list[Link[MessageModel]]

    class Settings:
        name = "chat_rooms"

    class Config:
        schema_extra = {
            "example": {
                "participants": ["user_1", "user_2", "user_3"],
            }
        }
