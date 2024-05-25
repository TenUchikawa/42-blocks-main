import asyncio
from typing import Optional

import requests

from blocks_duo.Board import Board
from blocks_duo.FinishedReason import FinishedReason
from blocks_duo.Player import Player


class View:

    def __init__(self, base_url: str):
        self.__base_url = base_url

    @property
    def base_url(self) -> str:
        return self.__base_url

    async def post_result(self, result: str):
        if self.base_url == '':
            return

        url = self.base_url + '/blocksview/result'
        request = {
            'winName': result
        }
        try:
            response = requests.post(url, json=request)  # POSTリクエストを送信
            if response.status_code == 200:
                print('勝敗データが正常に送信されました。')
            else:
                print(f'エラー: {response.status_code}')
            # viewモードの場合は待ちを入れる（見やすくするため）
        except Exception as e:
            print(e)

    async def post_win(self, winner: Optional[Player], reason: FinishedReason):
        if self.base_url == '':
            return

        if winner is None:
            result = 'draw'
        else:
            result = f'{winner.player_name} win'
            if reason == FinishedReason.illegal_placement:
                result += '（相手の反則負け）'

        await self.post_result(result)

    async def post_view(self, player1: Player, player2: Player, board: Board, score: dict[str, int]):
        if self.base_url == '':
            return

        data = board.now_board().tolist()

        p1block_list = player1.usable_blocks()
        p1_data = [item.name for item in p1block_list]

        p2block_list = player2.usable_blocks()
        p2_data = [item.name for item in p2block_list]
        url = self.base_url + '/blocksview'
        request = {
            'p1Name': player1.player_name,
            'p2Name': player2.player_name,
            'p1piece': p1_data,
            'p2piece': p2_data,
            'board': data,
            'score': {}
        }

        for player_name in score:
            request['score'][player_name] = score[player_name]

        try:
            response = requests.post(url, json=request)  # POSTリクエストを送信
            if response.status_code == 200:
                print('データが正常に送信されました。')
            else:
                print(f'エラー: {response.status_code}')
            # viewモードの場合は待ちを入れる（見やすくするため）
        except Exception as e:
            print(e)

        await self.view_wait(2)

    @staticmethod
    async def view_wait(wait: int = 1):
        await asyncio.sleep(wait)
        