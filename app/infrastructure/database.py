from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user import UserModel


class MongoDB:
    _CLIENT = AsyncIOMotorClient("mongodb://admin:1234@mongo:27017/")

    @classmethod
    async def init_db(cls):
        await init_beanie(database=cls._CLIENT.db_name, document_models=[UserModel])
