from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.core.auth import decode_access_token, user_id_from_token
from src.schema.user import UserResponseSchema
from src.usecase.get_user_usecase import GetUserUsecase
from src.usecase.get_users_usecase import GetUsersUsecase

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users(
    _: Annotated[dict, Depends(decode_access_token)],
    usecase: Annotated[GetUsersUsecase, Depends(GetUsersUsecase)],
) -> JSONResponse:
    users = await usecase()
    users_data = [
        UserResponseSchema(
            id=str(user.id),
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        ).model_dump()
        for user in users
    ]
    return JSONResponse(status_code=status.HTTP_200_OK, content=users_data)


@router.get("/me")
async def get_me(
    current_user: Annotated[dict, Depends(user_id_from_token)],
    usecase: Annotated[GetUsersUsecase, Depends(GetUserUsecase)],
):
    user = await usecase(current_user)
    user_data = UserResponseSchema(
        id=str(user.id),
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    ).model_dump()
    return JSONResponse(status_code=status.HTTP_200_OK, content=user_data)


@router.get("/{user_id}")
async def get_user_by_id(
    user_id: str,
    _: Annotated[dict, Depends(decode_access_token)],
    usecase: Annotated[GetUsersUsecase, Depends(GetUserUsecase)],
):
    user = await usecase(user_id)
    user_data = UserResponseSchema(
        id=str(user.id),
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    ).model_dump()
    return JSONResponse(status_code=status.HTTP_200_OK, content=user_data)
