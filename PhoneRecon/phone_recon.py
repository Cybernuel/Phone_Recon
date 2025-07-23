from modules.truecaller_lookup import truecaller_lookup
from modules.leak_check import check_leaks
from modules.google_dork import google_dork
from modules.telegram_check import check_telegram
from modules.utils import banner

def main():
    banner()
    phone = input("[?] Enter phone number (e.g. +234813xxxxxxx): ").strip()

    print("\n[+] Looking up name and carrier info...")
    truecaller_lookup(phone)

    print("\n[+] Checking Google dorks...")
    google_dork(phone)

    print("\n[+] Checking Telegram presence...")
    check_telegram(phone)

    print("\n[+] Checking leaked breaches...")
    check_leaks(phone)

    print("\n[+] Manual step: Try saving the number in WhatsApp to see name/photo.")

if __name__ == "__main__":
    main()
