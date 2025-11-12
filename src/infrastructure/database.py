from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import MONGO_DB
from src.model.message import MessageModel
from src.model.room import RoomModel
from src.model.user import UserModel


class MongoDB:
    _CLIENT = AsyncIOMotorClient(MONGO_DB.DATABASE_URL)
    _DB = _CLIENT[MONGO_DB.DATABASE_NAME]

    @classmethod
    async def init_db(cls):
        await init_beanie(
            database=cls._DB,
            document_models=[UserModel, RoomModel, MessageModel],
        )

    @classmethod
    def close(cls):
        cls._CLIENT.close()
