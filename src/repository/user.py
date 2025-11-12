from beanie import PydanticObjectId

from src.model.user import UserModel
from src.schema.user import UserSchema


class UserRepository:
    @staticmethod
    async def create(user: UserSchema) -> UserModel:
        new_user = UserModel(**user.model_dump())
        await new_user.insert()
        return new_user

    @staticmethod
    async def find_by_name(username: str) -> UserModel:
        user = await UserModel.find({"username": username}).first_or_none()
        return user

    @staticmethod
    async def find_by_id(user_id: str) -> UserModel:
        user = await UserModel.get(PydanticObjectId(user_id))
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
