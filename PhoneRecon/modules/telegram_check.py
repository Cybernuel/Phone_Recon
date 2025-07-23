import requests

def check_telegram(phone):
    print("    [!] Checking if number is linked to Telegram...")

    try:
        username = phone.replace("+", "")
        url = f"https://t.me/{username}"

        res = requests.get(url)
        if "If you have Telegram, you can contact" in res.text:
            print(f"    [+] Telegram profile seems to exist: {url}")
        else:
            print("    [-] Not found on Telegram (or private account).")
    except Exception as e:
        print(f"    [x] Error: {str(e)}")
