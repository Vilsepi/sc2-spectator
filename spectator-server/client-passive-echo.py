#!/usr/bin/env python

import asyncio
import uuid
import websockets

async def hello():
    async with websockets.connect('ws://localhost:9000') as websocket:
        while True:
            response = await websocket.recv()
            print(response)

asyncio.get_event_loop().run_until_complete(hello())
print("Passive echo client started, printing all received messages")
asyncio.get_event_loop().run_forever()
