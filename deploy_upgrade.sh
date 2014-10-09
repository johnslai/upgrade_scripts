#!/bin/bash
bud_ip=192.168.1.134
scp upgrade.py root@${bud_ip}:
ssh root@${bud_ip} /home/root/upgrade.py
