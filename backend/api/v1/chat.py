from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.core.websocket_manager import websocket_manager

router = APIRouter(prefix="/chat")

# import json

# from backend.dao.message import MessageRepo
# from backend.dao.room import RoomRepo
# from backend.dao.user_dao import UserDAO


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str):
    await websocket_manager.connect(websocket, token)

    try:
        while True:
            _ = await websocket.receive_text()
            # msg_json = json.loads(msg)
            # data = await UserDAO.find_all()

            # room = await RoomRepo.create("kek", data)

            # await MessageRepo.create(msg_json["message"], data[0], room)

            await websocket_manager.broadcast("placeholder", token)
    except WebSocketDisconnect:
        websocket_manager.disconnect(token)
