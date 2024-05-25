from __future__ import annotations
import asyncio
import websockets
from ss_player.Blocks import Blocks
from ss_player.Board import Board
from ss_player.Logic import Logic 
from ss_player.Player import Player




class PlayerClient:
    def __init__(self, player_number: int, socket: websockets.WebSocketClientProtocol, loop: asyncio.AbstractEventLoop):
        self._loop = loop
        self._socket = socket
        self._player_number = player_number
        self.player = Player(player_number)
        self.blocks = Blocks()
        self.board = Board()
        self.logic = Logic()
        self.p1Actions = ['R244', 'B037', 'J266', 'M149', 'O763', 'R0A3', 'F0C6', 'K113', 'T021', 'L5D2', 'G251', 'E291', 'D057', 'A053']
        self.p2Actions = ['R699', 'B098', 'N0A5', 'L659', 'K33B', 'J027', 'E2B9', 'C267', 'U07C', 'M3AD', 'O2BB', 'R41C']
        self.p1turn = 0
        self.p2turn = 0

    @property
    def player_number(self) -> int:
        return self._player_number

    async def close(self):
        await self._socket.close()

    async def play(self):
        while True:
            board_str = await self._socket.recv()
            action = self.create_action(board_str)
            await self._socket.send(action)
            if action == 'X000':
                raise SystemExit




    def create_action(self, board_str):
        actions: list[str]
        turn: int
        self.board.set_board(board_str)
        

        self.logic.get_available_actions(self.board,self.blocks,self.player)

        if self.player_number == 1:
            actions = self.p1Actions
            turn = self.p1turn
            self.p1turn += 1
        else:
            actions = self.p2Actions
            turn = self.p2turn
            self.p2turn += 1

        if len(actions) > turn:
            return actions[turn]
        else:
            # パスを選択
            return 'X000'
    
    @staticmethod
    async def create(url: str, loop: asyncio.AbstractEventLoop) -> PlayerClient:
        socket = await websockets.connect(url)
        print('PlayerClient: connected')
        player_number = await socket.recv()
        print(f'player_number: {player_number}')
        return PlayerClient(int(player_number), socket, loop)
