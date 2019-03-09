import asyncio
import websockets
import datetime
import random


class StateSender:
    def __init__(self, bot):
        self.bot = bot

    async def _send_websocket_message(self, message):
        async with websockets.connect('ws://localhost:9000') as websocket:
            await websocket.send(message)

    async def send(self):
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await self._send_websocket_message(now)
