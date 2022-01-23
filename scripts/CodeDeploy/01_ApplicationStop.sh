#!/bin/bash -e
source /home/ubuntu/.profile

# codedeploy-agentがフリーズすることがあるため予め再起動させる
sudo systemctl restart codedeploy-agent.service