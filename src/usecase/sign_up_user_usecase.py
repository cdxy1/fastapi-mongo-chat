from dataclasses import dataclass

from src.model.user import UserModel
from src.schema.user import UserSchema
from src.service.auth import AuthService


@dataclass
class SignUpUserUsecase:
    async def __call__(self, user: UserSchema) -> UserModel:
        return await AuthService.register(user)
