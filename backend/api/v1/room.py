import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.core.websocket_manager import websocket_manager
from backend.usecase.send_direct_message_usecase import SendDirectMessageUsecase

router = APIRouter(prefix="/chat")


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str):
    await websocket_manager.connect(websocket, token)

    try:
        while True:
            data = await websocket.receive_text()
            deserlized_data = json.loads(data)
            usecase = SendDirectMessageUsecase()
            users = await usecase(
                token, deserlized_data["receiver"], deserlized_data["message"]
            )

            for user in users:
                await websocket_manager.broadcast(
                    deserlized_data["message"], user.username
                )
    except WebSocketDisconnect:
        websocket_manager.disconnect(token)
