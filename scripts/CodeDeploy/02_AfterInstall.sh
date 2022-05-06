#!/bin/bash -e
source /home/ubuntu/.profile

# 仮想環境起動
source /home/ubuntu/discriminator/venv/bin/activate

# pythonライブラリインストール
pip install -r /home/ubuntu/discriminator/requirement/base.txt
deactivate

# Nginx, gunicorn再起動
sudo systemctl restart nginx
sudo systemctl restart gunicorn