
from ss_player.Block import Block
from ss_player.BlockType import BlockType
from ss_player.BlockRotation import BlockRotation
import numpy as np

class Blocks:
    def __init__(self):
        self.blocks: list[Block] = []
        for block_type in BlockType:
            for block_rotation in BlockRotation:
                dup = False
                for block in self.blocks:
                    new_block = Block(block_type, block_rotation)
                    if block.block_type == block_type and np.array_equal(block.block_map, new_block.block_map):
                        dup = True
                        break
                if not dup:
                    # 重複していない場合のみ追加
                    self.blocks.append(Block(block_type, block_rotation))

        self.blocks = list(reversed(self.blocks))
        x_block = self.blocks[0]
        self.blocks = [self.blocks[i] for i in range(1, len(self.blocks))]
        self.blocks.append(x_block)


    # 使用するブロックを削除する
    def block_used(self,block_type:BlockType):
        # for で回しているリストの内容をremoveすると想定外の挙動になる
        # 以下のような書き方にする
        self.blocks = [block for block in self.blocks 
                        if block.block_type != block_type]


if __name__ == "__main__":

    blocks = Blocks()
    for block in blocks.blocks:
        # if block.block_type == BlockType.A:
        print(block.block_type)
        print(block.block_map)
    # print(len(blocks.blocks))

    # blocks.block_used(BlockType.A)
    # print(len(blocks.blocks))
    # for block in blocks.blocks:
    #     if block.block_type == BlockType.A:
    #         print(block.block_type, block.block_map)
        
    

