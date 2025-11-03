from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.core.websocket_manager import websocket_manager

router = APIRouter(prefix="/chat")


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str):
    await websocket_manager.connect(websocket, token)

    try:
        while True:
            data = await websocket.receive_text()

            # sender = await UserRepo.find_by_name(token)
            # receiver = await UserRepo.find_by_name(json.loads(data)["receiver"])

            # room = await RoomService.create_p2p_room(sender, receiver)

            # _ = await MessageService.create_message(
            #     json.loads(data)["message"], sender, room
            # )

            await websocket_manager.broadcast(data, token)
    except WebSocketDisconnect:
        websocket_manager.disconnect(token)
