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

    class Config:
        schema_extra = {
            "example": {
                "sender_id": "user_123",
                "chat_id": "chat_456",
                "content": "Hello World!",
                "timestamp": "2025-05-29T15:45:00Z",
                "is_read": False,
            }
        }
