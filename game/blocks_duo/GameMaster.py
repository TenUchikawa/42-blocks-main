from __future__ import annotations
import asyncio
import os
import sys
from enum import IntEnum
from typing import Tuple, Optional

from blocks_duo.BattleRecord import BattleRecord
from blocks_duo.Block import Block
from blocks_duo.BlockType import BlockType
from blocks_duo.Board import Board
from blocks_duo.FinishedReason import FinishedReason
from blocks_duo.GameFinishedException import GameFinishedException
from blocks_duo.Player import Player
from blocks_duo.PlayerFactory import PlayerFactory
from blocks_duo.Position import Position
from blocks_duo.View import View
from blocks_duo.WebsocketServer import WebsocketServer

TIMEOUT_SEC = 10


class Turn(IntEnum):
    Player1 = 1
    Player2 = 2


class Master:
    def __init__(self, server: WebsocketServer, p1: Player, p2: Player, loop: asyncio.AbstractEventLoop, mode: str):
        self.__server = server
        self.__loop = loop
        self.__p1 = p1
        self.__p2 = p2
        self.__turn = Turn.Player1
        self.__board = Board()
        self.__mode = mode
        self.__records = BattleRecord(p1, p2)
        self.__score = {p1.player_name: 0, p2.player_name: 0}
        if mode == 'view':
            self.__view = View('http://localhost:8000/api')
        else:
            self.__view = View('')

    @property
    def player1(self) -> Player:
        return self.__p1

    @property
    def player2(self) -> Player:
        return self.__p2

    @property
    def board(self) -> Board:
        return self.__board
    
    @property
    def mode(self) -> str:
        return self.__mode

    @staticmethod
    async def create_game(server: WebsocketServer, p1_target: str, p2_target: str,
                          loop: asyncio.AbstractEventLoop, mode: str) -> Master:
        p1_name = p1_target
        p2_name = p2_target
        if p1_target == p2_target:
            p1_name += "_1"
            p2_name += "_2"

        p1 = await PlayerFactory.create(server, 1, p1_target, p1_name, loop)
        p2 = await PlayerFactory.create(server, 2, p2_target, p2_name, loop)
        return Master(server, p1, p2, loop, mode)

    async def switch_players(self):
        p1, p2 = (self.player2, self.player1)
        self.__p1 = await PlayerFactory.create(self.__server, 1, p1.target, p1.player_name, self.__loop)
        self.__p2 = await PlayerFactory.create(self.__server, 2, p2.target, p2.player_name, self.__loop)
        self.__board = Board()
        self.__records.clear()
        self.__turn = Turn.Player1

    async def start_match(self):
        round_ = 1
        while round_ < 6:
            print(f'start round {round_}')
            winner_name = await self.start_game(round_)

            self.__score[winner_name] += 1
            if self.__score[winner_name] > 2:
                break
            await self.switch_players()
            await asyncio.sleep(5)
            round_ += 1
        await self.print_score()

    async def start_game(self, round_: int) -> Optional[str]:
        winner: Optional[Player] = None
        finished_reason = FinishedReason.normal
        try:
            turn = 1
            print(f'turn {turn}.')
            # init view
            await self.__view.post_result('')
            await self.print_board()

            await self.first_turn()
            await self.print_board()

            while True:
                if not self.__p1.active and not self.__p2.active:
                    break

                turn += 1
                current_player = self.__p1 if self.__turn == Turn.Player1 else self.__p2

                print(f'turn {turn}.')
                print(f'player {current_player.player_number} action')

                await self.turn_action(current_player)
                await self.print_board()

                self.__turn = Turn.Player1 if self.__turn == Turn.Player2 else Turn.Player2

            winner = self.get_winner_player()
        except GameFinishedException as e:
            await self.print_board()
            winner = e.winner
            finished_reason = e.reason
        except Exception as e:
            print(e)

        await self.print_winner(winner, finished_reason)
        self.__records.add_result(winner)
        self.__records.output(self.log_file_name(round_))
        return winner.player_name if winner is not None else None

    async def first_turn(self):
        await self.first_turn_action(self.player1)
        await self.print_board()
        await self.first_turn_action(self.player2)

    async def first_turn_action(self, player: Player):
        async def action() -> Tuple[Block, Position]:
            await player.send_board(self.board)
            return await player.recv_input()

        try:
            block, position = await asyncio.wait_for(action(), TIMEOUT_SEC)
            player.use_block(block)
            self.board.try_place_first_block(player, block, position)

        except Exception as e:
            print(e)
            raise GameFinishedException(self.get_winner(loser=player), FinishedReason.illegal_placement)

    async def turn_action(self, player: Player):
        if not player.active:
            return

        async def action() -> Tuple[Block, Position]:
            await player.send_board(self.board)
            return await player.recv_input()

        try:
            block, position = await asyncio.wait_for(action(), TIMEOUT_SEC)
            print(block.block_type)
            print(position.x)
            print(position.y)
            if not block.block_type == BlockType.X:
                player.use_block(block)
                self.board.try_place_block(player, block, position)
            else:
                player.active = False
        except Exception as e:
            print(e)
            raise GameFinishedException(self.get_winner(loser=player), FinishedReason.illegal_placement)

    def get_winner(self, loser: Optional[Player]):
        if loser:
            return self.player1 if loser.player_number == 2 else self.player2
        else:
            return self.get_winner_player()
    
    def get_winner_player(self) -> Optional[Player]:
        p1_point = self.board.get_point(self.player1)
        p2_point = self.board.get_point(self.player2)
        if p1_point == p2_point:
            return None
        elif p1_point > p2_point:
            return self.player1
        else:
            return self.player2

    async def print_board(self):
        print(self.board.to_print_string())
        await self.__view.post_view(self.player1, self.player2, self.board, self.__score)

    async def print_score(self):
        print(f'finished.')
        print(f'score')
        for name in self.__score:
            print(f'{name}: {self.__score[name]}')
        await self.__view.post_view(self.player1, self.player2, self.board, self.__score)

    async def print_winner(self, winner: Optional[Player], finished_reason: FinishedReason):
        if winner is None:
            print('draw')
        else:
            print(f'player {winner.player_number} win '
                  f'{"（相手の反則負け）" if finished_reason == FinishedReason.illegal_placement else ""}.')

        await self.__view.post_win(winner, finished_reason)

    def log_file_name(self, round_: int) -> str:
        return '_'.join([name for name in self.__score]) + f'_{round_}.log'


def main():
    player1_target = sys.argv[1]
    player2_target = sys.argv[2]
    mode = ""
    if len(sys.argv) == 4:
        mode = sys.argv[3]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = WebsocketServer(loop)

    loop.run_until_complete(server.start())
    try:
        master = loop.run_until_complete(Master.create_game(server, player1_target, player2_target, loop, mode))
        loop.run_until_complete(master.start_match())
    except SystemExit:
        print('game close')
    except Exception as e:
        print(e)

    finally:
        server.stop()
        loop.stop()


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    main()
