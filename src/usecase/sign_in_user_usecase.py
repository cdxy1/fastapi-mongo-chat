from dataclasses import dataclass

from src.service.auth import AuthService


@dataclass
class SignInUserUsecase:
    async def __call__(self, username: str, password: str) -> dict[str, str]:
        return await AuthService.login(username, password)
