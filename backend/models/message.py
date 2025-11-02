from datetime import datetime

from beanie import Document, Link

from backend.models.room import RoomModel
from backend.models.user import UserModel


class MessageModel(Document):
    content: str
    sender: Link[UserModel]
    room: Link[RoomModel]
    timestamp: datetime = datetime.utcnow()
    is_read: bool = False

    class Settings:
        name = "messages"
