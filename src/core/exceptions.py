from fastapi import status
from fastapi.exceptions import HTTPException


class HTTPDuplicateException(HTTPException):
    def __init__(self):
        super().__init__(status.HTTP_409_CONFLICT, "Duplicate error", None)


class HTTPUnauthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status.HTTP_401_UNAUTHORIZED, "Unauthorized", None)


class TokenInvalidException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class TokenDecodeException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class RedisConnectionException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class UserNotFoundException(HTTPException):
    def __init__(self, message: str = "User not found"):
        super().__init__(status.HTTP_404_NOT_FOUND, message, None)

    def to_dict(self):
        return {"content": self.detail, "status_code": self.status_code}


class InvalidCredentialsException(HTTPException):
    def __init__(self, message: str = "Invalid username or password"):
        super().__init__(status.HTTP_401_UNAUTHORIZED, message, None)


class RefreshTokenNotFoundException(HTTPException):
    def __init__(self, message: str = "Refresh token not found"):
        super().__init__(status.HTTP_401_UNAUTHORIZED, message, None)


class UserAlreadyExistsException(HTTPException):
    def __init__(self, message: str = "User already exists"):
        super().__init__(status.HTTP_409_CONFLICT, message, None)


class RoomNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status.HTTP_404_NOT_FOUND, "Room not found", None)


class UnauthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status.HTTP_401_UNAUTHORIZED, "unauthorized", None)


class InvalidUserIdException(Exception): ...
