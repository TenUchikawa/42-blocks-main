from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Optional

from ss_player.Block import Block
from ss_player.BlockRotation import BlockRotation
from ss_player.BlockType import BlockType
from ss_player.Position import Position

class Player:
    def __init__(self, player_number: int):
        self.__player_number = player_number
        self.__usable_blocks = [b for b in BlockType]
        self.__active = True

    @property
    def player_number(self) -> int:
        return self.__player_number
    
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


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
