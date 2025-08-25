def calculate_tired_pricing(quantity: int) -> int:
    if quantity <= 0:
        raise ValueError()
    elif quantity <= 2:
        subscription_price = 299
    elif quantity <= 10:
        subscription_price = 239
    elif quantity <= 25:
        subscription_price = 219
    elif quantity <= 50:
        subscription_price = 199
    else:
        subscription_price = 149

    return quantity * subscription_price
