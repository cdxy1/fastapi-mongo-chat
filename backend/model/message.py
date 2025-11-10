from datetime import datetime

from beanie import Document, Link

from backend.model.room import RoomModel
from backend.model.user import UserModel


class MessageModel(Document):
    content: str
    sender: Link[UserModel]
    room: Link[RoomModel]
    timestamp: datetime = datetime.utcnow()
    is_read: bool = False

    class Settings:
        name = "messages"
