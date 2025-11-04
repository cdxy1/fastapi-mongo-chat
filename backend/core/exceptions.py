from fastapi import status
from fastapi.exceptions import HTTPException


class HTTPDuplicateException(HTTPException):
    def __init__(self):
        super().__init__(status.HTTP_409_CONFLICT, "Duplicate error", None)


class HTTPUnauthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status.HTTP_401_UNAUTHORIZED, "Unauthorized", None)
