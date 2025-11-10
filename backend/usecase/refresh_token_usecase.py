from dataclasses import dataclass

from backend.service.auth import AuthService


@dataclass
class RefreshTokenUsecase:
    async def __call__(self, user_id: str) -> dict[str, str]:
        return await AuthService.refresh_token(user_id)
