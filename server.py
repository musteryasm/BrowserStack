import asyncio
import websockets
import os

LOG_FILE_PATH = './test.log'
UPDATE_INTERVAL = 1
clients = set()
LAST_READ_POSITION = 0
LAST_MODIFIED_TIME = 0

async def read_log_file():
    global LAST_READ_POSITION, LAST_MODIFIED_TIME
    while True:
        try:
            current_modified_time = os.path.getmtime(LOG_FILE_PATH)
            if current_modified_time != LAST_MODIFIED_TIME:
                LAST_MODIFIED_TIME = current_modified_time

                with open(LOG_FILE_PATH, 'r') as file:
                    file.seek(LAST_READ_POSITION)
                    new_lines = file.readlines()
                    LAST_READ_POSITION = file.tell()

                if new_lines:
                    message = ''.join(new_lines)
                    print(f"Broadcasting new lines: {message}")
                    await broadcast(message)
        except Exception as e:
            print(f"Error reading log file: {e}")

        await asyncio.sleep(UPDATE_INTERVAL)

async def broadcast(message):
    to_remove = set()
    for client in clients:
        try:
            await client.send(message)
        except websockets.ConnectionClosed:
            to_remove.add(client)
    clients.difference_update(to_remove)

async def handle_client(websocket, path):
    global LAST_READ_POSITION
    clients.add(websocket)
    try:
        with open(LOG_FILE_PATH, 'r') as file:
            file.seek(max(0, LAST_READ_POSITION - 1024))
            lines = file.readlines()[-10:]  # last 10 lines
            await websocket.send(''.join(lines))

        async for _ in websocket:
            pass

    except websockets.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")
    finally:
        clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, 'localhost', 2003)

    # Run the log file reading task concurrently
    await asyncio.gather(
        read_log_file(),
        server.wait_closed()
    )

if __name__ == "__main__":
    asyncio.run(main())
