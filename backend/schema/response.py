from pydantic import BaseModel


class ResponseSchema(BaseModel):
    detail: str


class AccessTokenResponseSchema(ResponseSchema):
    access_token: str


class AuthResponseSchema(AccessTokenResponseSchema):
    refresh_token: str
    token_type: str
