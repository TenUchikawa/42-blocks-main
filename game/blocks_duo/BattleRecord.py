from __future__ import annotations

import csv
from typing import Optional

from blocks_duo.Player import Player


class BattleRecord:

    player1_name: str
    player2_name: str
    records: [(str, str)] = []
    result: str = ''

    def __init__(self, player1: Player, player2: Player):
        self.player1_name = player1.player_name
        self.player2_name = player2.player_name

    def add_record(self, player: Player, turn: str):
        self.records.append((f'{player.player_number}', turn))

    def add_result(self, winner: Optional[Player]):
        if winner is None:
            self.result = 'draw'
        else:
            self.result = f'winner is {winner.player_name}'

    def clear(self):
        self.records.clear()
        self.result = ''

    def output(self, target):
        with open(target, mode='w') as fp:
            writer = csv.writer(fp)

            writer.writerow(f'player 1: {self.player1_name}')
            writer.writerow(f'player 2: {self.player2_name}')
            record_str_list = [f'{record[0]}: {record[1]}' for record in self.records]
            writer.writerows(record_str_list)
            writer.writerow(self.result)

    @staticmethod
    def read_record(target: str) -> BattleRecord:
        pass
