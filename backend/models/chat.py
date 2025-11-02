from beanie import Document, Link

from backend.models.user import UserModel


class ChatRoomModel(Document):
    name: str
    participants: list[Link[UserModel]]

    class Settings:
        name = "chat_rooms"

    class Config:
        schema_extra = {
            "example": {
                "participants": ["user_1", "user_2", "user_3"],
            }
        }
