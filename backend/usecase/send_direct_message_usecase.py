from dataclasses import dataclass

from backend.models.user import UserModel
from backend.service.message import MessageService
from backend.service.room import RoomService
from backend.service.user import UserService


@dataclass
class SendDirectMessageUsecase:
    async def __call__(self, sender: str, reciver, msg: str) -> list[UserModel]:
        sender = await UserService.get_user(sender)
        reciver = await UserService.get_user(reciver)

        room = await RoomService.get_or_create_p2p_room(sender, reciver)

        await MessageService.create_message(msg, sender, room)

        users = await RoomService.get_room_users(room.name)

        return users
