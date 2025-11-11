from dataclasses import dataclass

from src.model.user import UserModel
from src.service.user import UserService


@dataclass
class GetUserUsecase:
    async def __call__(self, user_id: str) -> UserModel:
        return await UserService.get_user_by_id(user_id)
