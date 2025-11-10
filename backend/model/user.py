from typing import Annotated

from beanie import Document, Indexed


class UserModel(Document):
    username: Annotated[str, Indexed(unique=True)]
    first_name: str
    last_name: str
    password: str

    class Settings:
        name = "users"
