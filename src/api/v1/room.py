import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.core.websocket_manager import websocket_manager
from src.service.user import UserService
from src.usecase.send_direct_message_usecase import SendDirectMessageUsecase
from src.utils.security import decode_token

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str):
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        user = await UserService.get_user_by_id(user_id)
        username = user.username
    except Exception:
        await websocket.close()
        return

    await websocket_manager.connect(websocket, username)

    try:
        while True:
            data = await websocket.receive_text()
            deserlized_data = json.loads(data)

            if deserlized_data.get("receiver") and deserlized_data.get("message"):
                usecase = SendDirectMessageUsecase()
                users = await usecase(
                    username, deserlized_data["receiver"], deserlized_data["message"]
                )

                for user in users:
                    await websocket_manager.broadcast(
                        {"message": deserlized_data["message"]}, user.username
                    )
    except WebSocketDisconnect:
        websocket_manager.disconnect(username)
