from datetime import datetime

from beanie import Document, Link

from src.model.room import RoomModel
from src.model.user import UserModel


class MessageModel(Document):
    content: str
    sender: Link[UserModel]
    room: Link[RoomModel]
    timestamp: datetime = datetime.utcnow()
    is_read: bool = False

    class Settings:
        name = "messages"
