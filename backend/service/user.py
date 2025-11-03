from backend.models.user import UserModel
from backend.repository.user import UserRepo


class UserService:
    async def get_user(name: str) -> UserModel:
        user = await UserRepo.find_by_name(name)

        return user
