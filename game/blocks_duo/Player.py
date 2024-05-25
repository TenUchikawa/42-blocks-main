from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Optional
from websockets import WebSocketServerProtocol

from blocks_duo.Block import Block
from blocks_duo.BlockRotation import BlockRotation
from blocks_duo.BlockType import BlockType
from blocks_duo.Position import Position

if TYPE_CHECKING:
    from Board import Board
    from blocks_duo.BattleRecord import BattleRecord


class Player:
    def __init__(self, player_number: int, target: str, player_name: str, connection: WebSocketServerProtocol):
        self.__target = target
        self.__player_name = player_name
        self.__player_number = player_number
        self.__usable_blocks = [b for b in BlockType]
        self.__connection = connection
        self.__active = True
        self.__record: Optional[BattleRecord] = None

    @property
    def target(self) -> str:
        return self.__target

    @property
    def player_number(self) -> int:
        return self.__player_number
    
    @property
    def player_name(self) -> str:
        return self.__player_name
    
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    def set_record(self, record: BattleRecord):
        self.__record = record

    async def send_player_number(self):
        await self.__connection.send(f'{self.player_number}')

    async def send_board(self, board: Board):
        await self.__connection.send(board.to_print_string())

    async def recv_input(self) -> Tuple[Block, Position]:
        player_request = await self.__connection.recv()
        block, position = self._parse_request(player_request.upper())
        return block, position

    def _parse_request(self, player_request: str) -> Tuple[Block, Position]:
        if self.__record:
            self.__record.add_record(self, player_request)

        block_type = player_request[0]
        block_rotation = int(player_request[1])
        position_x = int(player_request[2], 16)
        position_y = int(player_request[3], 16)
        return Block(BlockType(block_type), BlockRotation(block_rotation)), Position(position_x, position_y)

    def can_use_block(self, block: Block) -> bool:
        return block.block_type in self.__usable_blocks

    def use_block(self, block: Block):
        if block.block_type not in self.__usable_blocks:
            raise ValueError("passed block is not usable.")
        self.__usable_blocks.remove(block.block_type)
    
    def usable_blocks(self) -> list[BlockType]:
        return self.__usable_blocks
