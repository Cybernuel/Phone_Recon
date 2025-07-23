import requests

def truecaller_lookup(phone):
    api_key = "YOUR_NUMLOOKUPAPI_KEY"  # Get from https://numlookupapi.com/
    url = f"https://api.numlookupapi.com/v1/validate/{phone}?apikey={api_key}"

    try:
        res = requests.get(url)
        data = res.json()

        if data.get("valid"):
            print(f"    [+] Name: {data.get('name') or 'Unknown'}")
            print(f"    [+] Country: {data.get('country_name')}")
            print(f"    [+] Line Type: {data.get('line_type')}")
            print(f"    [+] Carrier: {data.get('carrier')}")
        else:
            print("    [-] Invalid or unlisted number.")
    except Exception as e:
        print(f"    [x] Error: {str(e)}")
