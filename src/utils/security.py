from typing import Any

import jwt
from passlib.context import CryptContext

from src.core.config import SECURITY

pwd_context = CryptContext(["bcrypt"])


def generate_refresh_token(data: str) -> str:
    encoded_jwt = jwt.encode(
        data,
        SECURITY.SECRET_KEY,
        SECURITY.ALGORITHM,
    )

    return encoded_jwt


def decode_token(token: str) -> Any:
    return jwt.decode(token, SECURITY.SECRET_KEY, SECURITY.ALGORITHM)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
