import requests


def check_leaks(phone):
   
    print(f"[!] Checking leaks using HaveIBeenPwned (email recommended)...")
    email_or_phone = input("    [?] Enter email linked to phone (or use phone): ").strip()

    api_key = "YOUR_HIBP_API_KEY"
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "PhoneRecon"
    }

    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email_or_phone}?truncateResponse=false"

    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            breaches = res.json()
            print(f"    [+] Found {len(breaches)} breaches:")
            for breach in breaches:
                print(f"       - {breach['Name']} ({breach['BreachDate']})")
        elif res.status_code == 404:
            print("[+] No breaches found.")
        else:
            print(f"    [-] Error: {res.status_code}")
    except Exception as e:
        print(f"[x] Error: {str(e)}")
