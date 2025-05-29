from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document


class MessageModel(Document):
    sender_id: str
    chat_id: UUID = uuid4()
    content: str
    timestamp: datetime = datetime.utcnow
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
