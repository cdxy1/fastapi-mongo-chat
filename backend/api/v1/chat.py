from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.core.websocket_manager import websocket_manager

router = APIRouter()


@router.websocket("/{room_id}/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket, room_id: int, user_id: int, username: str
):
    await websocket_manager.connect(websocket, room_id, user_id)
    await websocket_manager.broadcast(
        f"{username} (ID: {user_id}) присоединился к чату.", room_id, user_id
    )

    try:
        while True:
            data = await websocket.receive_text()
            await websocket_manager.broadcast(
                f"{username} (ID: {user_id}): {data}", room_id, user_id
            )
    except WebSocketDisconnect:
        websocket_manager.disconnect(room_id, user_id)
        await websocket_manager.broadcast(
            f"{username} (ID: {user_id}) покинул чат.", room_id, user_id
        )
