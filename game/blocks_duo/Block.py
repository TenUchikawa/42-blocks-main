import numpy as np

from blocks_duo.BlockType import BlockType
from blocks_duo.BlockRotation import BlockRotation


class Block:

    def __init__(self, block_type: BlockType, block_rotation: BlockRotation):
        self.__block_type = block_type
        temp_map = block_type.block_map
        for _ in range(0, (4 - block_rotation.rotation_count()) % 4):
            temp_map = np.rot90(temp_map)
        if block_rotation.reversed():
            temp_map = np.fliplr(temp_map)
        self.__block_map = temp_map

    @property
    def block_type(self) -> BlockType:
        return self.__block_type

    @property
    def block_map(self):
        return self.__block_map

    @property
    def shape_x(self) -> int:
        return self.__block_map.shape[1]

    @property
    def shape_y(self) -> int:
        return self.__block_map.shape[0]
    


if __name__ == "__main__":
    # for block_rotation in BlockRotation:
    #     block = Block("R", block_rotation)
    #     print(block.block_type)
    #     print(block.block_map)
    #     print(block.shape_x)
    #     print(block.shape_y)
    #     print("")

    block = Block("R", BlockRotation.Rotation_0)
    print(block.block_type)
    print(block.block_map)
    print("")