from datetime import datetime

from beanie import Document, Link

from backend.models.chat import ChatRoomModel
from backend.models.user import UserModel


class MessageModel(Document):
    content: str
    sender: Link[UserModel]
    room: Link[ChatRoomModel]
    timestamp: datetime = datetime.utcnow()
    is_read: bool = False

    class Settings:
        name = "messages"
