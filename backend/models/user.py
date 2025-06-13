from typing import Annotated

from beanie import Document, Indexed


class UserModel(Document):
    username: Annotated[str, Indexed(unique=True)]
    first_name: str
    last_name: str
    password: str

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "username": "JohnDoe123",
                "first_name": "John",
                "last_name": "Doe",
                "password": "t46g3748gd2y8gasfkbasfak",
            }
        }
