import webbrowser

def google_dork(phone):
    queries = [
        f'"{phone}" site:pastebin.com',
        f'"{phone}" site:facebook.com',
        f'"{phone}" site:twitter.com',
        f'"{phone}" site:linkedin.com',
        f'"{phone}" site:instagram.com',
        f'"{phone}" site:medium.com',
        f'"{phone}" site:nairaland.com',
    ]
    for q in queries:
        webbrowser.open(f"https://www.google.com/search?q={q}")
