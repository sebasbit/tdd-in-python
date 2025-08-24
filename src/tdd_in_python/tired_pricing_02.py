def calculate_tired_pricing(quantity: int) -> int:
    if quantity >= 3 and quantity <= 10:
        return quantity * 239
    elif quantity >= 11 and quantity <= 25:
        return quantity * 219
    elif quantity == 26:
        return 5174
    return quantity * 299
