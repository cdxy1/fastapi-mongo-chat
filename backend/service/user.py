from backend.models.user import UserModel
from backend.repository.user import UserRepository


class UserService:
    async def get_user(name: str) -> UserModel:
        user = await UserRepository.find_by_name(name)

        return user
