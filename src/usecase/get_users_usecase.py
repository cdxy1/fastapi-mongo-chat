from dataclasses import dataclass

from src.model.user import UserModel
from src.service.user import UserService


@dataclass
class GetUsersUsecase:
    async def __call__(self) -> list[UserModel]:
        return await UserService.get_all_users()
