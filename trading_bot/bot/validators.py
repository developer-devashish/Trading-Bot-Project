def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")


def validate_quantity(qty):
    if float(qty) <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None or float(price) <= 0:
            raise ValueError("LIMIT orders require valid price")