#!/bin/bash
sudo apt update && sudo apt upgrade -y

sudo apt install python3 -y

sudo apt install curl -y

curl -Ls https://raw.githubusercontent.com/oomplay/Simply_Download_Youtube_Videos/main/youtube-dlauto.py > autoinstall.py

python3 autoinstall.py

rm -r autoinstall.py

clear
