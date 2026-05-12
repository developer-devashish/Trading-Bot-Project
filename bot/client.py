import os
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://demo-api.binance.com"

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def get_server_time():
    url = BASE_URL + "/api/v3/time"
    return requests.get(url).json()["serverTime"]


def sign(params):
    query_string = urlencode(params)
    return hmac.new(
        API_SECRET.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()


def send_request(method, path, params):
    params["timestamp"] = get_server_time()
    params["signature"] = sign(params)

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    url = BASE_URL + path

    if method == "POST":
        res = requests.post(url, headers=headers, params=params)
    else:
        res = requests.get(url, headers=headers, params=params)

    return res.json()