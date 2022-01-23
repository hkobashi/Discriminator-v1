#!/bin/bash -e
source /home/ubuntu/.profile

# 仮想環境起動
source /home/ubuntu/venv/bin/activate

# pythonライブラリインストール
pip install -r requirement/base.txt
deactivate