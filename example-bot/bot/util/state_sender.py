import asyncio
import websockets
import json

class StateSender:
    def __init__(self, bot):
        self.bot = bot

    async def _send_websocket_message(self, message):
        async with websockets.connect('ws://localhost:9000') as websocket:
            await websocket.send(message)
            websocket.close()

    async def send(self):
        own_units = self.bot.units
        enemy_units = self.bot.known_enemy_units

        payload = {
            "own_units": [
                {
                    "tag": unit.tag,
                    "type": str(unit.type_id).replace("UnitTypeId.", ""),
                    "pos_x": unit.position.x,
                    "pos_y": unit.position.y
                } for unit in own_units],
            "enemy_units": [
                {
                    "tag": unit.tag,
                    "type": str(unit.type_id).replace("UnitTypeId.", ""),
                    "pos_x": unit.position.x,
                    "pos_y": unit.position.y,
                    "is_visible": unit.is_visible
                } for unit in enemy_units]
        }

        await self._send_websocket_message(json.dumps(payload))
