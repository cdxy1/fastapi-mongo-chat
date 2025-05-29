from beanie import Document, Indexed
from datetime import datetime
from pydantic import Field
from typing import List, Optional


class ChatRoomModel(Document):
    participants: list

    class Settings:
        name = "chat_rooms"

    class Config:
        schema_extra = {
            "example": {
                "participants": ["user_1", "user_2", "user_3"],
            }
        }
