def calculate_tired_pricing(quantity: int) -> int:
    if quantity <= 2:
        return quantity * 299
    elif quantity <= 10:
        return quantity * 239
    elif quantity <= 25:
        return quantity * 219
    elif quantity <= 50:
        return quantity * 199
    else:
        return quantity * 149
