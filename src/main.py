from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.router import router as api_router
from src.infrastructure.database import MongoDB
from src.infrastructure.redis import REDIS_CLIENT


@asynccontextmanager
async def lifespan(app: FastAPI):
    await REDIS_CLIENT.connect()
    await MongoDB().init_db()
    yield
    MongoDB.close()
    await REDIS_CLIENT.close()


app = FastAPI(lifespan=lifespan, title="Websocket Chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
