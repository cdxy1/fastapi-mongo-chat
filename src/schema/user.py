from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str


class UserResponseSchema(BaseModel):
    id: str
    username: str
    first_name: str
    last_name: str
