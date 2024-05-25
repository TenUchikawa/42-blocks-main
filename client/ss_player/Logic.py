
from ss_player.Board import Board
from ss_player.Blocks import Blocks
from ss_player.Position import Position
from ss_player.Player import Player
from time import sleep
import numpy as np




# Board example o = player1, x = player2
#  123456789ABCDE
# 1..............
# 2..............
# 3..............
# 4...o..........
# 5..ooo.........
# 6...o..........
# 7..............
# 8..............
# 9..............
# A.........x....
# B..............
# C..............
# D..............
# E..............

xystr = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E"]

class Logic:
    def get_available_actions(self,board:Board,blocks:Blocks,player:Player):

        print(board.now_board())
        is_first = not np.any(board.now_board() == player.player_number)

        print("is_first")
        print(is_first)
        # sleep(2)
        if(is_first):
            if(player.player_number == 1):
                return "R244"
            else:
                return "R699"

        for block in blocks.blocks:
            for x in range(board.shape_x):
                for y in range(board.shape_y):
                    padded_block = None
                    try:
                        padded_block = board.PaddedBlock(board,block,Position(x,y))
                    except Exception as e:
                        # TODO Errorハンドリング追加。　今は-1の場合にエラーになるのでTryCatchで回避
                        # print(e.__str__ == "index can't contain negative values")
                        # sleep(5)
                        continue

                    # print(board.can_place(player,padded_block))
                    if(board.can_place(player,padded_block)):
                        
                        result = f"{block.block_type.value}{block.block_rotation.value}{xystr[x]}{xystr[y-1]}"
                        # block.block_used(block.block_type)
                        print(result)
                        print(board.now_board())
                        print(padded_block.block_map)

                        print("padded_block.corner_map")
                        print(padded_block.corner_map)
                        print("padded_block.block_map")
                        print(padded_block.block_map)
                        print("padded_block.edge_map")
                        print(padded_block.edge_map)
                        print("padded_block.map")
                        print(padded_block.map)
                        

                        
                        # sleep(10)
                        
                        
                        return result
                    


if __name__ == '__main__':
    str = """123456789ABCDE
1..............
2..............
3..............
4..............
5..............
6..............
7..............
8..............
9..............
A..............
B..............
C..............
D..............
E.............."""
    board = Board(str)
    blocks = Blocks()
    print(board.now_board())
    logic = Logic()
    player = Player(1)
    logic.get_available_actions(board,blocks,player)



    pass




        