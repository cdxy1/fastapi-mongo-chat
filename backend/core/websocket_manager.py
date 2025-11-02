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

    async def broadcast(self, message: dict, user: str):
        if conn := self.active_connections.get(user):
            # message_with_class = {
            #     "time": str(datetime.now()),
            #     "user": user,
            #     "text": message,
            # }
            await conn.send_json(message)


websocket_manager = ConnectionManager()
