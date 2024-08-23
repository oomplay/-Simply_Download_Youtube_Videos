import time
#import urllib.request
import random
import os

cls = lambda: os.system("clear")
cls()

LOGO = r'''
///    __   __         _____      _            ____                      _                 _     ///
///    \ \ / /__  _   |_   _|   _| |__   ___  |  _ \  _____      ___ __ | | ___   __ _  __| |    ///
///     \ V / _ \| | | || || | | | '_ \ / _ \ | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |    ///
///      | | (_) | |_| || || |_| | |_) |  __/ | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |    ///
///      |_|\___/ \__,_||_| \__,_|_.__/ \___| |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|    ///
'''

CREATE = r'''
/* .----------------------------------------------. */
/* |  ___   ___  __  __   ____  _        _ __   __| */
/* | / _ \ / _ \|  \/  | |  _ \| |      / \\ \ / /| */
/* || | | | | | | |\/| | | |_) | |     / _ \\ V / | */
/* || |_| | |_| | |  | | |  __/| |___ / ___ \| |  | */
/* | \___/ \___/|_|  |_| |_|   |_____/_/   \_\_|  | */
/* '----------------------------------------------' */
'''

TYPE = r'''
▶ Select resolution
▶ [1] Video 360p
▶ [2] Video 480p
▶ [3] Video 720p
▶ [4] Video 1080p
▶ [5] Video 2160p
'''

print(LOGO)
time.sleep(0.5)
print("CREATED BY ")
time.sleep(0.5)
print(CREATE)
time.sleep(2)
cls()
URL = input("Enter your video link: ")
time.sleep(1)
print(TYPE)


SELECT = int(input("Enter 1-5: "))
#PXURL = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
#Proxy from "https://github.com/TheSpeedX/PROXY-List"
#with urllib.request.urlopen(PXURL) as response:
#    proxies = response.read().decode().splitlines()
#   random_proxy = random.choice(proxies)

quality_options = {
    1: "bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]",
    2: "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]",
    3: "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]",
    4: "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]",
    5: "bestvideo[height<=2160][ext=mp4]+bestaudio[ext=m4a]"
}


if SELECT in quality_options:
    print(f"DOWNLOAD VIDEO")
    time.sleep(1)
    cls()
    os.system(f'yt-dlp -f "{quality_options[SELECT]}" --output "./Youtube_video/%(title)s.%(ext)s" "{URL}"')
    #os.system(f'yt-dlp -f "{quality_options[SELECT]}" --output "./Youtube_video/%(title)s.%(ext)s" --proxy "socks5://{random_proxy}" "{URL}"')
    time.sleep(0.2)
else:
    print('Invalid selection. Try again!')
