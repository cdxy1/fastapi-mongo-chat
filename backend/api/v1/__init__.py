from fastapi import APIRouter

from backend.api.v1.auth import router as auth_router
from backend.api.v1.chat import router as chat_router
from backend.api.v1.user import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(chat_router)
router.include_router(auth_router)
router.include_router(user_router)
