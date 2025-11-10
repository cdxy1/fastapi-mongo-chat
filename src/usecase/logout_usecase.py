from dataclasses import dataclass

from src.service.auth import AuthService


@dataclass
class LogoutUsecase:
    async def __call__(self, user_id: str) -> None:
        await AuthService.logout(user_id)
