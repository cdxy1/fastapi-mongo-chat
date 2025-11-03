from dataclasses import dataclass

from backend.service.message import MessageService
from backend.service.room import RoomService
from backend.service.user import UserService


@dataclass
class SendDirectMessageUsecase:
    async def __call__(self, sender: str, reciver, msg: str):
        sender = await UserService.get_user(sender)
        reciver = await UserService.get_user(reciver)

        if not await RoomService.is_room_exists(sender, reciver):
            room = await RoomService.create_p2p_room(sender, reciver)
        else:
            room = await RoomService.get_p2p_room(sender, reciver)

        await MessageService.create_message(msg, sender, room)

        users = await RoomService.get_room_users(room.name)

        return users, msg
