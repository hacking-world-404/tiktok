
from os import system as c
import time
import random

#------------- COLORS -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{R}
▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄ 
▐▌  ▐▌ ▄     ▀▄  ▀ ▄     ▐▌  ▐▌
▐▛▀▀▀▌ █ ▄▄▄  █     ▀▄▄▄ ▐▛▀▀▀▌
▐▌  ▐▌ ▀▄▄▄▀ ▄▄▀   ▀▄▄▄▀ ▐▌  ▐▌
{Y}    HACKING WORLD - TIKTOK AUTO FOLLOW PRANK
{A}-------------------------------------------------
""")

#------------- LOADING FUNCTION -------------#
def loading(msg):
    for i in range(3):
        print(f"{C}{msg}{'.'*i}")
        time.sleep(0.5)
        c('clear')
        logo()

#------------- FOLLOW FUNCTION -------------#
def auto_follow():
    logo()
    user = input(f"{C}[+] Enter TikTok Username: ")
    loading("Connecting to TikTok Server")
    print(f"{G}[✓] Username Verified: {user}")
    time.sleep(1)

    followers = random.randint(5000, 50000)
    print(f"{Y}[*] Adding {followers} Followers to {user}...")
    time.sleep(2)

    for percent in range(0, 101, 10):
        print(f"{C}[*] Inject Progress: {percent}%")
        time.sleep(0.3)
        c('clear')
        logo()

    print(f"{G}[✓] Successfully Added {followers} Followers to {user}!")
    print(f"{P}[*] Please restart your TikTok app to see the updated followers.")
    input(f"\n{C}Press Enter To Exit...")

#------------- START TOOL -------------#
auto_follow()

