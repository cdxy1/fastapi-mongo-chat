import os
from datetime import timedelta
from typing import Optional

from dotenv import load_dotenv
from fastapi import HTTPException
from redis import ConnectionError, Redis
from redis import asyncio as aioredis
from starlette import status

load_dotenv()


class RedisClient:
    def __init__(self):
        self.redis_url = os.getenv("REDIS_URL")
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
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Redis is not available.",
            )

    async def get_value(self, key) -> Optional[str]:
        try:
            return await self.redis.get(f"refresh:{key}")
        except ConnectionError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Redis is not available.",
            )

    async def delete_value(self, key) -> None:
        try:
            await self.redis.delete(f"refresh:{key}")
        except ConnectionError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Redis is not available.",
            )


redis_client = RedisClient()
