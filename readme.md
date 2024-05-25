# 環境構築（サンプル対戦時）
python3 -m venv ssvenv
source ssvenv/bin/activate
pip install -U ./game
pip install -U ./client
start_blocksduo ss_five ss_five view
※./gameでゲーム本体が、./clientでサンプルプレイヤーがインストールされる
ゲーム本体：blocks_duo_ss
サンプルプレイヤー：ss_five

# サンプルプレイヤーでの実行
start_blocksduo ss_five ss_five
