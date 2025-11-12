from jwt.exceptions import ExpiredSignatureError

from src.core.exceptions import (
    InvalidUserIdException,
    UnauthorizedException,
    UserNotFoundException,
)


def to_http_error(exc):
    match exc:
        case InvalidUserIdException():
            raise UserNotFoundException
        case ExpiredSignatureError():
            raise UnauthorizedException
        case _:
            raise Exception
