from dataclasses import dataclass

from backend.model.user import UserModel
from backend.schema.user import UserSchema
from backend.service.auth import AuthService


@dataclass
class SignUpUserUsecase:
    async def __call__(self, user: UserSchema) -> UserModel:
        return await AuthService.register(user)
