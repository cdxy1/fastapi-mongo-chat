from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, ExpiredSignatureError

from backend.core.exceptions import TokenDecodeException, TokenInvalidException
from backend.infrastructure.redis import redis_client
from backend.utils.security import decode_token, generate_refresh_token

oauth2_schema = OAuth2PasswordBearer("/api/v1/auth/login")


def create_access_token(
    data: dict,
) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=30)
    to_encode.update({"exp": expire})

    encoded_jwt = generate_refresh_token(to_encode)

    return encoded_jwt


async def create_refresh_token(
    username: str,
) -> str:
    expire = timedelta(days=30)
    encoded_jwt = generate_refresh_token({"sub": username})

    await redis_client.set_value(username, encoded_jwt, expire)

    return encoded_jwt


def decode_access_token(token: Annotated[str, Depends(oauth2_schema)]) -> dict:
    try:
        payload = decode_token(token)
        exp = payload.get("exp")

        if not exp or datetime.now() >= datetime.utcfromtimestamp(exp):
            raise TokenInvalidException
        return payload

    except DecodeError:
        raise TokenDecodeException


def user_id_from_token(token: Annotated[str, Depends(oauth2_schema)]) -> dict:
    try:
        payload = decode_token(token)
        user = payload.get("sub")

        return user

    except DecodeError:
        raise TokenDecodeException
    except ExpiredSignatureError:
        raise TokenInvalidException
