#!/bin/bash
# 仮想環境削除
rm -rf /home/ubuntu/discriminator/venv
virtualenv /home/ubuntu/discriminator/venv

# pythonライブラリインストール
pip install -r /home/ubuntu/discriminator/requirement/base.txt

# 仮想環境起動
source /home/ubuntu/discriminator/venv/bin/activate
deactivate