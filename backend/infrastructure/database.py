from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from backend.core.config import MONGO_DB
from backend.models.user import UserModel


class MongoDB:
    _CLIENT = AsyncIOMotorClient(MONGO_DB.DATABASE_URL)

    @classmethod
    async def init_db(cls):
        await init_beanie(database=cls._CLIENT.db_name, document_models=[UserModel])
