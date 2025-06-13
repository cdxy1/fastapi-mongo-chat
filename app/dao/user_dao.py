from app.models.user import UserModel
from app.schemas.user import UserSchema
from app.utils.auth import hash_password


class UserDAO:
    @staticmethod
    async def create(user: UserSchema):
        user.password = hash_password(user.password)
        new_user = UserModel(**user.model_dump())
        await new_user.insert()
        return new_user

    @staticmethod
    async def find_by_name(username: str):
        user = await UserModel.find({"username": username}).first_or_none()
        return user

    @staticmethod
    async def read_all() -> list["UserModel"]:
        users_cursor = UserModel.find_all()
        users = await users_cursor.to_list()
        return users

    @staticmethod
    def update(): ...

    @staticmethod
    def delete(): ...
