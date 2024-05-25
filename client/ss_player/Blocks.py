
from ss_player.Block import Block
from ss_player.BlockType import BlockType
from ss_player.BlockRotation import BlockRotation
import numpy as np
import random
import itertools

class Blocks:
    def __init__(self):
        self.blocks: list[Block] = []
        raw_blocks_list: list[Block] = []
        for block_type in BlockType:
            for block_rotation in BlockRotation:
                dup = False
                for block in raw_blocks_list:
                    new_block = Block(block_type, block_rotation)
                    if block.block_type == block_type and np.array_equal(block.block_map, new_block.block_map):
                        dup = True
                        break
                if not dup:
                    # 重複していない場合のみ追加
                    raw_blocks_list.append(Block(block_type, block_rotation))

        one_part_blocks = [raw_blocks_list[0]]
        two_part_blocks = [raw_blocks_list[1]]
        three_part_blocks = raw_blocks_list[2:4]
        four_part_blocks = raw_blocks_list[4:9]
        five_part_blocks = raw_blocks_list[9:-1]

        all_block_lists = [five_part_blocks, four_part_blocks, three_part_blocks, two_part_blocks, one_part_blocks]
        for block_list in all_block_lists:
            random.shuffle(block_list)

        for blocks in all_block_lists:
            for block in blocks:
                self.blocks.append(block)
        
        print("all_block_list len ")
        print(len(self.blocks))
        print(self.blocks)
        

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
        
    

