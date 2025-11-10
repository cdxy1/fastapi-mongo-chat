from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.core.auth import decode_access_token
from src.usecase.get_users_usecase import GetUsersUsecase

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users(
    current_user: Annotated[dict, Depends(decode_access_token)],
) -> JSONResponse:
    usecase = GetUsersUsecase()
    users = await usecase()
    users_data = [
        {
            "id": str(user.id),
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        for user in users
    ]
    return JSONResponse(status_code=status.HTTP_200_OK, content=users_data)
