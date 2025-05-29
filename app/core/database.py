from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import MongoConfig


class MongoDB:
    _CLIENT = AsyncIOMotorClient(MongoConfig.DATABASE_URL)

    @classmethod
    async def init_db(cls):
        await init_beanie(database=cls._CLIENT.db_name, document_models=[...])  # Models
