from beanie import Document, Link

from src.model.user import UserModel


class RoomModel(Document):
    name: str
    participants: list[Link[UserModel]]

    class Settings:
        name = "chat_rooms"
