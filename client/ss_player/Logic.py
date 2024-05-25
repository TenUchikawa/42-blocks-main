
from ss_player.Board import Board
from ss_player.Blocks import Blocks
from ss_player.Position import Position
from ss_player.Player import Player
from ss_player.BlockType import BlockType
from ss_player.Block import Block
from ss_player.timer import Timer
from time import sleep
import numpy as np


DEPTH = 1


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

xystr = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E"]

class Logic:
    def get_available_actions(self,board:Board,blocks:Blocks,player:Player):

        print(board.now_board())
        is_first = not np.any(board.now_board() == player.player_number)

        # print("is_first")
        # print(is_first)
        # sleep(2)
        if(is_first):
            blocks.block_used(BlockType.R)
            if(player.player_number == 1):
                return "R244"
            else:
                return "R699"
        
        available_indexes = board.get_available_indexes(player)

        cost = 0
        for block in blocks.blocks:
            for x in range(1,board.shape_x+1): # available_indexesとの整合性取れてない？
                for y in range(1,board.shape_y+1):
                    if (x,y) not in available_indexes:
                        continue
                    cost += 1

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
                        
                        result = f"{block.block_type.value}{block.block_rotation.value}{xystr[x-1]}{xystr[y-1]}"
                        blocks.block_used(block.block_type)
                        
                        print("cost",cost)

                        
                        return result
        return "X000"
    

    def count_can_put_position_num(self, board: Board, player: Player) -> int:
        cnt = 0
        for x in range(board.shape_x):
            for y in range(board.shape_y):
                if 0 <= x - 1 and board.now_board()[y][x - 1] != player.player_number:
                    continue
                if x + 1 < board.shape_x and board.now_board()[y][x + 1] != player.player_number:
                    continue
                if 0 <= y - 1 and board.now_board()[y - 1][x] != player.player_number:
                    continue
                if y + 1 < board.shape_y and board.now_board()[y + 1][x] != player.player_number:
                    continue
                if (0 <= y - 1 < 14 and 0 <= x - 1 < 14 and board.now_board()[y - 1][x - 1] == player.player_number) or \
                    (0 <= y - 1 < 14 and 0 <= x + 1 < 14 and board.now_board()[y - 1][x + 1] == player.player_number) or \
                    (0 <= y + 1 < 14 and 0 <= x + 1 < 14 and board.now_board()[y + 1][x + 1] == player.player_number) or \
                    (0 <= y + 1 < 14 and 0 <= x - 1 < 14 and board.now_board()[y + 1][x - 1]) == player.player_number:
                    cnt += 1
        return cnt
    
    
    def evaluate(self, board: Board, player: Player) -> int:
        return self.count_can_put_position_num(board, player)


    def get_search_value(self, blocks: Blocks, board: Board, player: Player, depth: int, my_turn: bool, timer: Timer) -> tuple[bool, int, str]:
        # print("get_search_value is called") # for debug
        this_value = self.evaluate(board, player)

        if DEPTH <= depth: return True, this_value, None

        value = 0
        best_option = ''
        for block in blocks.blocks:
            available_indexes = board.get_available_indexes(player)
            print(block.block_map)
            print(available_indexes)
            for x in range(board.shape_x):
                for y in range(board.shape_y):
                    if (x, y) not in available_indexes: continue
                    print(x, y)
                    try:
                        padded_block = board.PaddedBlock(board, block, Position(x + 1, y + 1))
                    except:
                        continue
                    if (not board.can_place(player, padded_block)): continue
                    print('can place')
                    board.place_block(player, padded_block) # blockをboardにセット
                    flag, child_value, _ = self.get_search_value(blocks, board, player, depth + 1, not my_turn, timer)
                    if not flag: return False, None, f"{block.block_type.value}{str(block.block_rotation.value)}{xystr[x]}{xystr[y]}"
                    if my_turn:
                        if child_value > value:
                            value = child_value
                            best_option = f"{block.block_type.value}{block.block_rotation.value}{xystr[x]}{xystr[y]}"
                    else:
                        if child_value < value:
                            value = child_value
                            best_option = f"{block.block_type.value}{str(block.block_rotation.value)}{xystr[x]}{xystr[y]}"
                    board.unplace_block(player, padded_block) # blockをboardからはずす
                    if not timer.check(): # タイムリミットが近づいたらその時に最も良いものを返す
                        return False, None, f"{block.block_type.value}{str(block.block_rotation.value)}{xystr[x]}{xystr[y]}"
            
        return True, this_value + value, best_option





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




        