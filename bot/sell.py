import time

from bot.market_data import get_market_price
from bot.orders import place_order


def run_sell():

    symbol = "BTCUSDT"
    quantity = 0.001

    buy_price = 80000

    target = buy_price + 50
    stoploss = buy_price - 50

    print(f"""
========================
BUY PRICE : {buy_price}
TARGET    : {target}
STOPLOSS  : {stoploss}
========================
""")

    print("\n📊 Monitoring Market...\n")

    while True:

        current_price = get_market_price(symbol)

        print(f"Current Price: {current_price}")

        # TARGET HIT
        if current_price >= target:

            print("\n✅ Target Reached")
            print("📤 Placing SELL Order...\n")

            order = place_order(
                symbol,
                "SELL",
                "MARKET",
                quantity
            )

            print(order)

            break

        # STOPLOSS HIT
        elif current_price <= stoploss:

            print("\n❌ Stoploss Hit")
            print("📤 Placing SELL Order...\n")

            order = place_order(
                symbol,
                "SELL",
                "MARKET",
                quantity
            )

            print(order)

            break

        time.sleep(5)