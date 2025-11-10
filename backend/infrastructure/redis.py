from datetime import timedelta
from typing import Optional

from redis import ConnectionError, Redis
from redis import asyncio as aioredis

from backend.core.config import REDIS
from backend.core.exceptions import RedisConnectionException


class RedisClient:
    def __init__(self):
        self.redis_url = REDIS.REDIS_URL
        self.redis: Optional[Redis | None] = None

    async def connect(self) -> None:
        self.redis = await aioredis.from_url(self.redis_url, decode_responses=True)

    async def close(self) -> None:
        if self.redis:
            await self.redis.close()

    async def set_value(self, key: str, value: str, expire: timedelta) -> None:
        try:
            await self.redis.setex(f"refresh:{key}", expire, value)
        except ConnectionError:
            raise RedisConnectionException

    async def get_value(self, key) -> Optional[str]:
        try:
            return await self.redis.get(f"refresh:{key}")
        except ConnectionError:
            raise RedisConnectionException

    async def delete_value(self, key) -> None:
        try:
            await self.redis.delete(f"refresh:{key}")
        except ConnectionError:
            raise RedisConnectionException


REDIS_CLIENT = RedisClient()
