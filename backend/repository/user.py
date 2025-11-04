from backend.models.user import UserModel
from backend.schema.user import UserSchema
from backend.utils.security import hash_password


class UserRepository:
    @staticmethod
    async def create(user: UserSchema) -> UserModel:
        user.password = hash_password(user.password)
        new_user = UserModel(**user.model_dump())
        await new_user.insert()
        return new_user

    @staticmethod
    async def find_by_name(username: str) -> UserModel:
        user = await UserModel.find({"username": username}).first_or_none()
        return user

    @staticmethod
    async def find_all() -> list["UserModel"]:
        users_cursor = UserModel.find_all()
        users = await users_cursor.to_list()
        return users

    @staticmethod
    def update(): ...

    @staticmethod
    def delete(): ...
