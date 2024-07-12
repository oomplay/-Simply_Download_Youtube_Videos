import time
import os
cls = lambda:os.system("clear")
cls()
LOGO = r'''
///        _         _          _           _        _ _  __   __         _____      _                ____  _         ///
///       / \  _   _| |_ ___   (_)_ __  ___| |_ __ _| | | \ \ / /__  _   |_   _|   _| |__   ___      |  _ \| |        ///
///      / _ \| | | | __/ _ \  | | '_ \/ __| __/ _` | | |  \ V / _ \| | | || || | | | '_ \ / _ \_____| | | | |        ///
///     / ___ \ |_| | || (_) | | | | | \__ \ || (_| | | |   | | (_) | |_| || || |_| | |_) |  __/_____| |_| | |___     ///
///    /_/   \_\__,_|\__\___/  |_|_| |_|___/\__\__,_|_|_|   |_|\___/ \__,_||_| \__,_|_.__/ \___|     |____/|_____|    ///
'''
print(LOGO),time.sleep(3),cls()
print("update_packages"),time.sleep(0.2),cls()
os.system('sudo apt update && sudo apt upgrade -y'),time.sleep(0.2),cls()

print("install_python"),time.sleep(2),cls()
os.system('apt install python -y'),time.sleep(0.2),cls()
os.system('apt install python3 -y'),time.sleep(0.2),cls()
os.system('apt install python3-pip -y'),time.sleep(0.2),cls()

print("install_ffmpeg"),time.sleep(2),cls()
os.system('apt install ffmpeg -y'),time.sleep(0.2),cls()

print("install_youtube_dl"),time.sleep(2),cls()
os.system('pip install yt-dlp'),time.sleep(0.2),cls()
os.system('pip install yt-dlp -U'),time.sleep(0.2),cls()
os.system(' mkdir -p Youtube_video'),time.sleep(0.2),cls()


#os.system('yt-dlp -f "bestvideo[height<=1440][ext=mp4]+bestaudio[ext=m4a]" --output "./TBvideo/%(title)s.%(ext)s" "https://youtu.be/Mcr_ja6WHCI?si=_jeV050cTA54AYJN"')


