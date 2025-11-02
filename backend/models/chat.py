from beanie import Document, Link

from backend.models.user import UserModel


class ChatRoomModel(Document):
    name: str
    participants: list[Link[UserModel]]

    class Settings:
        name = "chat_rooms"
