import asyncio
import websockets
import json

class StateSender:
    def __init__(self, bot):
        self.bot = bot
        self.map = self._get_map()

    def _get_map(self):
        blocked_points = []
        grid = self.bot.game_info.pathing_grid
        for y in range(grid.height):
            for x in range(grid.width):
                if not grid.is_set((x, y)):
                    blocked_points.append({
                        "x": x,
                        "y": y
                    })
        return blocked_points


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
                    "pos_y": unit.position.y,
                    "radius": unit.radius,
                    "health": unit.health_percentage,
                } for unit in own_units],
            "enemy_units": [
                {
                    "tag": unit.tag,
                    "type": str(unit.type_id).replace("UnitTypeId.", ""),
                    "pos_x": unit.position.x,
                    "pos_y": unit.position.y,
                    "radius": unit.radius,
                    "health": unit.health_percentage,
                    "is_visible": unit.is_visible
                } for unit in enemy_units],
            "map": self.map
        }

        await self._send_websocket_message(json.dumps(payload))
