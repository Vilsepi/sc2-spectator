#!/usr/bin/env python

import asyncio
import json
import logging
import websockets

logging.basicConfig()

CLIENTS = set()

async def send_state(state):
    if CLIENTS:
        await asyncio.wait([user.send(state) for user in CLIENTS])

async def register(websocket):
    print("New client connected")
    CLIENTS.add(websocket)

async def unregister(websocket):
    print("Client disconnected")
    CLIENTS.remove(websocket)

async def proxy(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            await send_state(message)
    finally:
        await unregister(websocket)

asyncio.get_event_loop().run_until_complete(websockets.serve(proxy, '0.0.0.0', 9000))
asyncio.get_event_loop().run_forever()
