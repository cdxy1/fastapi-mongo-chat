from fastapi import APIRouter

from src.api.v1.auth import router as auth_router
from src.api.v1.room import router as room_router
from src.api.v1.user import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(room_router)
router.include_router(auth_router)
router.include_router(user_router)
