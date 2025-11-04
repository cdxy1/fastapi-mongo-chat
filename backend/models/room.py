from enum import Enum

from beanie import Document, Link

from backend.models.user import UserModel


class RoomTypeEnum(Enum):
    P2P = 1
    GROUP = 2


class RoomModel(Document):
    name: str
    participants: list[Link[UserModel]]
    # type: RoomTypeEnum

    class Settings:
        name = "chat_rooms"
