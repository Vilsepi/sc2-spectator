#!/usr/bin/env python

import asyncio
import websockets
import datetime
import random

async def hello():
    async with websockets.connect('ws://localhost:9000') as websocket:
        while True:
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            await websocket.send(now)
            await asyncio.sleep(random.random() * 3)

asyncio.get_event_loop().run_until_complete(hello())
print("Mock bot client started, sending timestamps")
asyncio.get_event_loop().run_forever()
