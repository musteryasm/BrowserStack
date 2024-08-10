####testing codes
#####testing purpose only
##### main code in server.py

import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello there!")
        greeting = await websocket.recv()
        print(f"Received: {greeting}")

asyncio.run(hello('ws://localhost:2000'))

with open('test.log','r') as file:
	lines = file.readlines()
last= lines[-10:]
for line in last:
	print(line, end='')


LOG_FILE_PATH = './test.log'
LastRead = 0
LastModify = 0
UPDATE_INTERVAL = 1

async def read_log_file():
    global LastRead, LastModify
    while True:
            with open(LOG_FILE_PATH, 'r') as file:
                file.seek(LastRead)
                new_lines = file.readlines()
                LastRead = file.tell()