from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user: str):
        await websocket.accept()
        if user not in self.active_connections:
            self.active_connections[user] = websocket

    def disconnect(self, user: str):
        if user in self.active_connections:
            del self.active_connections[user]

    async def broadcast(self, message: str, user: str):
        if user in self.active_connections:
            for user_id, connection in self.active_connections.items():
                message_with_class = {
                    "user": user_id,
                    "text": message,
                }
                await connection.send_json(message_with_class)


websocket_manager = ConnectionManager()
