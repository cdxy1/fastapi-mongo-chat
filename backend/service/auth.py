from pymongo.errors import DuplicateKeyError

from backend.core.auth import (
    create_access_token,
    create_refresh_token,
)
from backend.core.exceptions import (
    InvalidCredentialsException,
    RefreshTokenNotFoundException,
    UserAlreadyExistsException,
)
from backend.infrastructure.redis import REDIS_CLIENT
from backend.model.user import UserModel
from backend.repository.user import UserRepository
from backend.schema.user import UserSchema
from backend.utils.security import hash_password, verify_password


class AuthService:
    @staticmethod
    async def register(user: UserSchema) -> UserModel:
        try:
            # Hash password before storing
            user_dict = user.model_dump()
            user_dict["password"] = hash_password(user_dict["password"])
            user_with_hashed_password = UserSchema(**user_dict)

            created_user = await UserRepository.create(user_with_hashed_password)
            return created_user
        except DuplicateKeyError:
            raise UserAlreadyExistsException()

    @staticmethod
    async def login(username: str, password: str) -> dict[str, str]:
        user = await UserRepository.find_by_name(username=username)

        if not user:
            raise InvalidCredentialsException()

        if not verify_password(password, user.password):
            raise InvalidCredentialsException()

        token = create_access_token({"sub": str(user.id)})
        refresh_token = await create_refresh_token(str(user.id))

        return {
            "access_token": token,
            "refresh_token": refresh_token,
        }

    @staticmethod
    async def refresh_token(user_id: str) -> dict[str, str]:
        refresh_token = await REDIS_CLIENT.get_value(user_id)

        if not refresh_token:
            raise RefreshTokenNotFoundException()

        payload = {"sub": user_id}
        access_token = create_access_token(payload)
        new_refresh_token = await create_refresh_token(user_id)

        return {
            "access_token": access_token,
            "refresh_token": new_refresh_token,
        }

    @staticmethod
    async def logout(user_id: str) -> None:
        await REDIS_CLIENT.delete_value(user_id)
