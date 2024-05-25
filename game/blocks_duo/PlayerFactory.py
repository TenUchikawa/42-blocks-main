import subprocess

import asyncio
import websockets

from blocks_duo.Player import Player
from blocks_duo.WebsocketServer import WebsocketServer


class PlayerFactory:
    @staticmethod
    async def create(server: WebsocketServer, player_number: int, target: str, name: str, loop: asyncio.AbstractEventLoop):
        future: asyncio.Future[Player] = loop.create_future()

        def on_connect(socket: websockets.WebSocketServerProtocol):
            player = Player(player_number, target, name, socket)

            print(f'player: {player_number} connected')
            future.set_result(player)

        server.set_callback(on_connect)
        loop.run_in_executor(None, PlayerFactory.start_client, target, server.server_url())

        try:
            player = await asyncio.wait_for(future, 20)
            await player.send_player_number()
            print(f'player {player_number} was created.')
            return player
        finally:
            server.clear_callback()

    @staticmethod
    def start_client(target: str, url: str):
        print(f'client_script={target}')
        args = [target, url]
        subprocess.run(args)
