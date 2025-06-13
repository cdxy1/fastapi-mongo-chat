from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.dao.user_dao import UserDAO
from app.infrastructure.redis_infra import redis_client
from app.schemas.response import (
    AccessTokenResponseSchema,
    AuthResponseSchema,
    ResponseSchema,
)
from app.schemas.user import UserSchema
from app.utils.auth import (
    create_access_token,
    create_refresh_token,
    decode_access_token,
    user_id_from_token,
    verify_password,
)

router = APIRouter(tags=["Auth"])


@router.post("/register")
async def register(
    user: UserSchema,
) -> JSONResponse:
    await UserDAO.create(user)
    response = ResponseSchema(detail="Success")
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=response.model_dump()
    )


@router.get("/get_users")
async def get_users():
    users = await UserDAO().read_all()
    return JSONResponse(status_code=status.HTTP_200_OK, content=users)


@router.post("/auth")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> JSONResponse:
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
    )

    user = await UserDAO.find_by_name(username=form_data.username)
    if user and verify_password(form_data.password, user.password):
        token = create_access_token({"sub": str(user.id)})
        refresh_token = await create_refresh_token(str(user.id))
        response = AuthResponseSchema(
            detail="Success",
            access_token=token,
            refresh_token=refresh_token,
            token_type="bearer",
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=response.model_dump()
        )
    else:
        raise credentials_exc


@router.post("/refresh")
async def refresh_access_token(
    current_user: Annotated[str, Depends(user_id_from_token)],
):
    exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    if not current_user:
        raise exc

    refresh_token = await redis_client.get_value(current_user)
    if not refresh_token:
        raise exc

    payload = {"sub": current_user}

    token = create_access_token(payload)
    response = AccessTokenResponseSchema(detail="Success", access_token=token)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response.model_dump())


@router.delete("/logout")
async def logout(
    current_user: Annotated[dict, Depends(decode_access_token)],
) -> JSONResponse:
    user_id = current_user.get("sub")
    await redis_client.delete_value(user_id)
    response = ResponseSchema(detail="Success")
    return JSONResponse(status_code=status.HTTP_200_OK, content=response.model_dump())
