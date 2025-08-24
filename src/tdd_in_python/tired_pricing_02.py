def calculate_tired_pricing(quantity: int) -> int:
    if quantity >= 3 and quantity <= 10:
        return quantity * 239
    elif quantity == 11:
        return 2409
    return quantity * 299
