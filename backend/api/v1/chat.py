from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.core.websocket_manager import websocket_manager

router = APIRouter(prefix="/chat")


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str):
    print(websocket.headers)
    await websocket_manager.connect(websocket, token)
    await websocket_manager.broadcast("placeholder", token)

    try:
        while True:
            data = await websocket.receive_text()
            await websocket_manager.broadcast(data, token)
    except WebSocketDisconnect:
        websocket_manager.disconnect(token)
        await websocket_manager.broadcast("placeholder", token)
