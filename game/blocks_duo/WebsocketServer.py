from typing import Optional

import asyncio
import websockets

DOMAIN = 'localhost'
PORT = 8088


class WebsocketServer:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop
        self.__server: Optional[websockets.WebSocketServer] = None
        self.__ws_connect_callback = None
        self.__server_loop = asyncio.new_event_loop()

    def __del__(self):
        self.stop()

    async def start(self):
        async def on_connect(websocket, path):
            # print(f'on_connect {websocket}')
            if self.__ws_connect_callback:
                self._loop.run_in_executor(None, self.__ws_connect_callback, websocket)
                await self._loop.create_future()

        self.__server = await websockets.serve(on_connect, DOMAIN, PORT)

    def stop(self):
        self.__server.close()

    def set_callback(self, on_connect):
        self.__ws_connect_callback = on_connect

    def clear_callback(self):
        self.__ws_connect_callback = None

    @staticmethod
    def server_url() -> str:
        return f'ws://{DOMAIN}:{PORT}'
