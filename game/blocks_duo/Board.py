from __future__ import annotations
import numpy as np

from blocks_duo.Block import Block
from blocks_duo.Player import Player
from blocks_duo.Position import Position

EmptyChar = '.'
Player1Char = 'o'
Player2Char = 'x'


class Board:
    def __init__(self):
        self.__board = np.zeros((14, 14), dtype=np.int64)
        pass

    def now_board(self):
        """
        現状のboardの状態を返す
        :return:
        """
        return self.__board

    @property
    def shape_x(self) -> int:
        return self.__board.shape[1]

    @property
    def shape_y(self) -> int:
        return self.__board.shape[0]
    
    def get_point(self, player: Player) -> int:
        score = 0
        if len(player.usable_blocks()) == 0:
            score += 20
        score += len(self.__board[self.__board == player.player_number])
        return score

    def try_place_first_block(self, player: Player, block: Block, position: Position):
        self.assert_range(block, position)
        padded_block = Board.PaddedBlock(self, block, position)
        if not self.can_place_first_block(player, padded_block):
            raise ValueError("invalid position")
        self.place_block(player, padded_block)

    def try_place_block(self, player: Player, block: Block, position: Position):
        self.assert_range(block, position)
        padded_block = Board.PaddedBlock(self, block, position)
        if not self.can_place(player, padded_block):
            raise ValueError("invalid position: cannot place")
        self.place_block(player, padded_block)

    def assert_range(self, block, position):
        if position.x < 0 or position.x + block.shape_x > self.shape_x:
            raise ValueError("invalid position")
        if position.y < 0 or position.y + block.shape_y > self.shape_y:
            raise ValueError("invalid position")

    def can_place(self, player: Player, padded_block: PaddedBlock) -> bool:
        if self.detect_collision(padded_block):
            return False
        if self.detect_side_connection(player, padded_block):
            return False
        return self.detect_corner_connection(player, padded_block)

    def can_place_first_block(self, player: Player, padded_block: PaddedBlock) -> bool:
        if player.player_number == 1 and padded_block.block_map[4, 4] == 1:
            return True
        if player.player_number == 2 and padded_block.block_map[9, 9] == 1:
            return True
        return False

    def detect_collision(self, padded_block: PaddedBlock) -> bool:
        collision_map = padded_block.block_map
        return self.__board.flatten().dot(collision_map.flatten()) > 0

    def detect_side_connection(self, player: Player, padded_block: PaddedBlock) -> bool:
        edge_map = padded_block.edge_map
        player_block_map = np.zeros(self.__board.shape, dtype=np.int64)
        player_block_map[self.__board == player.player_number] = 1
        return player_block_map.flatten().dot(edge_map.flatten()) > 0

    def detect_corner_connection(self, player: Player, padded_block: PaddedBlock) -> bool:
        corner_map = padded_block.corner_map
        player_block_map = np.zeros(self.__board.shape, dtype=np.int64)
        player_block_map[self.__board == player.player_number] = 1
        return player_block_map.flatten().dot(corner_map.flatten()) > 0

    def place_block(self, player: Player, padded_block: PaddedBlock):
        self.__board += padded_block.block_map * player.player_number

    def to_print_string(self) -> str:
        row_ids = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']

        ret: list[str] = [f' {"".join(row_ids)}']
        for row_id, row in zip(row_ids, self.__board):
            row_str = ''.join([
                Player1Char if b == 1 else
                Player2Char if b == 2 else
                EmptyChar
                for b in row])
            ret.append(f'{row_id}{"".join(row_str)}')
        return '\n'.join(ret)

    class PaddedBlock:

        def __init__(self, board: Board, block: Block, position: Position):
            pad_top = position.y
            pad_bottom = board.shape_y - (position.y + block.shape_y)
            pad_left = position.x
            pad_right = board.shape_x - (position.x + block.shape_x)
            self.__map = np.pad(block.block_map, ((pad_top, pad_bottom), (pad_left, pad_right)))
            self.__decorate_corner(self.__map)
            self.__decorate_edge(self.__map)

        @staticmethod
        def __decorate_corner(map_):
            corner_lt = np.array([[0, 0], [0, 1]])
            corner_rt = np.array([[0, 0], [1, 0]])
            corner_lb = np.array([[0, 1], [0, 0]])
            corner_rb = np.array([[1, 0], [0, 0]])

            corner_windows = np.lib.stride_tricks.sliding_window_view(map_, [2, 2], writeable=True)
            for corner_windows_row in corner_windows:
                for corner_window in corner_windows_row:
                    if np.all(corner_window == corner_lt):
                        corner_window[0, 0] = 2
                    elif np.all(corner_window == corner_rt):
                        corner_window[0, 1] = 2
                    elif np.all(corner_window == corner_lb):
                        corner_window[1, 0] = 2
                    elif np.all(corner_window == corner_rb):
                        corner_window[1, 1] = 2

        @staticmethod
        def __decorate_edge(map_):
            edge_left = np.array([[0, 1]])
            edge_right = np.array([[1, 0]])

            vertical_windows = np.lib.stride_tricks.sliding_window_view(map_, [1, 2], writeable=True)
            for vertical_windows_row in vertical_windows:
                for vertical_window in vertical_windows_row:
                    if np.all(vertical_window == edge_left):
                        vertical_window[0, 0] = 3
                    elif np.all(vertical_window == edge_right):
                        vertical_window[0, 1] = 3

            edge_top = np.array([[0], [1]])
            edge_bottom = np.array([[1], [0]])

            vertical_windows = np.lib.stride_tricks.sliding_window_view(map_, [2, 1], writeable=True)
            for vertical_windows_row in vertical_windows:
                for vertical_window in vertical_windows_row:
                    if np.all(vertical_window == edge_top):
                        vertical_window[0, 0] = 3
                    elif np.all(vertical_window == edge_bottom):
                        vertical_window[1, 0] = 3

        @property
        def map(self):
            return self.__map

        @property
        def block_map(self):
            map_ = np.zeros(self.__map.shape, dtype=np.int64)
            map_[self.__map == 1] = 1
            return map_

        @property
        def edge_map(self):
            map_ = np.zeros(self.__map.shape, dtype=np.int64)
            map_[self.__map == 3] = 1
            return map_

        @property
        def corner_map(self):
            map_ = np.zeros(self.__map.shape, dtype=np.int64)
            map_[self.__map == 2] = 1
            return map_
