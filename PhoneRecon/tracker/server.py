from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"[{now}] IP: {ip} | UA: {ua}\n"
    print(log_entry)

    with open("logs.txt", "a") as f:
        f.write(log_entry)

    return render_template('index.html')

@app.route('/location', methods=["POST"])
def location():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"[{now}] IP: {ip} | Location: ({lat}, {lon})\n"
    print(log_entry)

    with open("logs.txt", "a") as f:
        f.write(log_entry)

    return "Location logged"
