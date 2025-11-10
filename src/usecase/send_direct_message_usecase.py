from dataclasses import dataclass

from src.model.user import UserModel
from src.service.message import MessageService
from src.service.room import RoomService
from src.service.user import UserService


@dataclass
class SendDirectMessageUsecase:
    async def __call__(self, sender: str, receiver: str, msg: str) -> list[UserModel]:
        sender_user = await UserService.get_user(sender)
        receiver_user = await UserService.get_user(receiver)

        room = await RoomService.get_or_create_p2p_room(sender_user, receiver_user)

        await MessageService.create_message(msg, sender_user, room)

        users = await RoomService.get_room_users(room.name)

        recipients = list(filter(lambda user: user != sender_user, users))

        return recipients
