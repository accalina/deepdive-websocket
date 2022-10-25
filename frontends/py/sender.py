
import asyncio
import websockets

async def send_msg(message:str) -> str():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(message)
        print(await websocket.recv())

while True:
    user_input = input("user: ")
    asyncio.run(send_msg(user_input))