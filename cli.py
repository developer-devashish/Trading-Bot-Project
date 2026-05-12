import argparse

from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger
from bot.sell import run_sell


def main():

    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)
    parser.add_argument("--mode", required=True)

    args = parser.parse_args()

    try:

        # SELL BOT MODE
        if args.mode == "sell":

            run_sell()

            return

        # NORMAL ORDER MODE
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        print("\n📌 Order Summary:")
        print(vars(args))

        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        if "code" in order:

            print("\n❌ Order Failed")
            print(order)

        else:

            print("\n✅ Order Successful")
            print(f"Order ID: {order.get('orderId')}")
            print(f"Status: {order.get('status')}")
            print(f"Executed Qty: {order.get('executedQty')}")
            print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:

        print("\n❌ Order Failed")
        print(str(e))


if __name__ == "__main__":
    main()