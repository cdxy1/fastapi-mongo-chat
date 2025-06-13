from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.v1.auth import router as auth_router
from backend.api.v1.chat import router as chat_router
from backend.infrastructure.database import MongoDB
from backend.infrastructure.redis_infra import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.connect()
    await MongoDB().init_db()
    yield
    await redis_client.close()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chat_router)
app.include_router(auth_router)
