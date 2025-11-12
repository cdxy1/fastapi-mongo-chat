from src.model.user import UserModel
from src.repository.user import UserRepository


class UserService:
    @staticmethod
    async def get_user(name: str) -> UserModel:
        user = await UserRepository.find_by_name(name)

        return user

    @staticmethod
    async def get_user_by_id(user_id: str) -> UserModel:
        user = await UserRepository.find_by_id(user_id)
        return user

    @staticmethod
    async def get_all_users() -> list[UserModel]:
        users = await UserRepository.find_all()
        return users
