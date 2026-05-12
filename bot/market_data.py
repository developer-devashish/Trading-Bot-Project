import requests

BASE_URL = "https://api.binance.com"


def get_market_price(symbol):

    url = f"{BASE_URL}/api/v3/ticker/price"

    params = {
        "symbol": symbol
    }

    response = requests.get(url, params=params)

    data = response.json()

    return float(data["price"])