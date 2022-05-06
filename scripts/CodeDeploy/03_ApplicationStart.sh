#!/bin/bash -e
source /home/ubuntu/.profile

# 仮想環境を起動してDBマイグレーション
source /home/ubuntu/discriminator/venv/bin/activate
python /home/ubuntu/discriminator/manage.py migrate --settings config.settings.EC2
deactivate