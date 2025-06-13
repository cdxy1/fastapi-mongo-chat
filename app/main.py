from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.auth import router as auth_router

# from app.api.v1.chat import router as chat_router
from app.infrastructure.database import MongoDB
from app.infrastructure.redis_infra import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.connect()
    await MongoDB().init_db()
    yield
    await redis_client.close()


app = FastAPI(lifespan=lifespan)
# app.include_router(chat_router)
app.include_router(auth_router)
