from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.router import router as api_router
from backend.infrastructure.database import MongoDB
from backend.infrastructure.redis import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.connect()
    await MongoDB().init_db()
    yield
    MongoDB.close()
    await redis_client.close()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
