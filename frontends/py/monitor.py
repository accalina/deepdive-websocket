
import asyncio
import websockets

async def monitor():
    async with websockets.connect("ws://localhost:8765") as websocket:
        test = await websocket.recv()
        print(test)

for _ in range(2):
    asyncio.run(monitor())