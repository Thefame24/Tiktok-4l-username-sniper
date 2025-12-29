import random
import string
import time
import requests

# ================= SETTINGS =================
CHECK_DELAY = 0.0001       # seconds between checks (lower = faster, riskier)
TIMEOUT = 10
OUTPUT_FILE = "available_usernames.txt"
# ============================================

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ANSI colors
PURPLE = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# ================= ASCII ART =================
ASCII_ART = f"""
{PURPLE}
╭━━╮╭━━━┳━━━┳━━━━┳━━━┳━━━┳━━╮╭━━━┳━╮╭━╮╭━━━━┳━━━┳━━━┳╮
┃╭╮┃┃╭━━┫╭━╮┃╭╮╭╮┣╮╭╮┃╭━╮┃╭╮┃┃╭━╮┣╮╰╯╭╯┃╭╮╭╮┃╭━╮┃╭━╮┃┃
┃╰╯╰┫╰━━┫┃╱┃┣╯┃┃╰╯┃┃┃┃┃╱┃┃╰╯╰┫┃╱┃┃╰╮╭╯╱╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
┃╭━╮┃╭━━┫╰━╯┃╱┃┃╱╱┃┃┃┃╰━╯┃╭━╮┃┃╱┃┃╭╯╰╮╱╱╱┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
┃╰━╯┃╰━━┫╭━╮┃╱┃┃╱╭╯╰╯┃╭━╮┃╰━╯┃╰━╯┣╯╭╮╰╮╱╱┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
╰━━━┻━━━┻╯╱╰╯╱╰╯╱╰━━━┻╯╱╰┻━━━┻━━━┻━╯╰━╯╱╱╰╯╱╰━━━┻━━━┻━━━╯

   BeatDaBox Tools

        ⠀⠀⠀⣀⣤⣶⣶⣶⣤⣀
        ⠀⢀⣴⣿⡿⠟⠛⠛⠻⠿⢿⣿⣦⡀
        ⢀⣾⣿⠟⠁⠀⢀⣀⣀⡀⠀⠈⠙⢿⣷⡀
        ⣾⣿⠃⠀⢠⣾⣿⠿⠿⢿⣿⣷⡄⠀⠘⣿⣷
        ⣿⣿⠀⢀⣿⣿⣧⣀⣀⣠⣾⣿⡇⠀⠀⣿⣿
        ⢿⣿⣆⠀⠻⢿⣿⣿⣿⣿⡿⠟⠃⠀⢠⣿⡿
        ⠈⠻⢿⣷⣦⣄⣀⠈⠉⠉⠁⣀⣠⣴⣾⡿⠟⠁
"""
# ============================================

def random_username():
    return ''.join(random.choices(string.ascii_lowercase, k=4))

def check_username(username):
    url = f"https://www.tiktok.com/@{username}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 404:
            return "AVAILABLE"
        elif r.status_code == 200:
            return "TAKEN"
        else:
            return "UNKNOWN"
    except requests.RequestException:
        return "ERROR"

def main():
    checked = set()

    print(ASCII_ART + RESET)
    print("TikTok 4-letter username checker (INFINITE MODE)")
    print("Press CTRL + C to stop\n")

    while True:
        username = random_username()
        if username in checked:
            continue

        checked.add(username)
        status = check_username(username)

        if status == "AVAILABLE":
            print(f"{GREEN}[ AVAILABLE ] @{username}{RESET}")
            with open(OUTPUT_FILE, "a") as f:
                f.write(username + "\n")
        elif status == "TAKEN":
            print(f"{RED}[  TAKEN   ] @{username}{RESET}")
        else:
            print(f"[ UNKNOWN ] @{username}")

        time.sleep(CHECK_DELAY)

if __name__ == "__main__":
    main()
