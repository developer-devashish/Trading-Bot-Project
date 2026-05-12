from bot.market_data import get_market_price

price = get_market_price("BTCUSDT")

print(f"Current BTC Price: {price}")