#!/bin/bash
pkill -f app.py || true
nohup python3 /home/ec2-user/app/app.py > /home/ec2-user/app/app.log 2>&1 &
