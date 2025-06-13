from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str:WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        self.active_connections.pop(user_id)

    async def send_personal_message(
        self, user_id: str, message: str, websocket: WebSocket
    ):
        websocket = self.active_connections[user_id]
        if websocket:
            await websocket.send_text(message)


websocket_manager = ConnectionManager()
