from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.core.auth import decode_access_token, user_id_from_token
from src.schema.response import (
    AccessTokenResponseSchema,
    AuthResponseSchema,
    ResponseSchema,
)
from src.schema.user import UserSchema
from src.usecase.logout_usecase import LogoutUsecase
from src.usecase.refresh_token_usecase import RefreshTokenUsecase
from src.usecase.sign_in_user_usecase import SignInUserUsecase
from src.usecase.sign_up_user_usecase import SignUpUserUsecase

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(
    user: UserSchema,
) -> JSONResponse:
    usecase = SignUpUserUsecase()
    await usecase(user)
    response = ResponseSchema(detail="success")
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=response.model_dump()
    )


@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> JSONResponse:
    usecase = SignInUserUsecase()
    tokens = await usecase(form_data.username, form_data.password)

    token_response = AuthResponseSchema(
        detail="success",
        access_token=tokens.get("access_token"),
        token_type="bearer",
    )

    response = JSONResponse(
        status_code=status.HTTP_200_OK, content=token_response.model_dump()
    )

    response.set_cookie("refresh", tokens.get("refresh_token"), httponly=True)

    return response


@router.post("/refresh")
async def refresh_access_token(
    current_user: Annotated[str, Depends(user_id_from_token)],
) -> JSONResponse:
    usecase = RefreshTokenUsecase()
    tokens = await usecase(current_user)
    token_response = AccessTokenResponseSchema(
        detail="success", access_token=tokens.get("access_token")
    )

    response = JSONResponse(
        status_code=status.HTTP_200_OK, content=token_response.model_dump()
    )

    response.set_cookie("refresh", tokens.get("refresh_token"), httponly=True)

    return response


@router.delete("/logout")
async def logout(
    current_user: Annotated[dict, Depends(decode_access_token)],
) -> JSONResponse:
    user_id = current_user.get("sub")
    usecase = LogoutUsecase()
    await usecase(user_id)
    response = ResponseSchema(detail="success")
    return JSONResponse(status_code=status.HTTP_200_OK, content=response.model_dump())
