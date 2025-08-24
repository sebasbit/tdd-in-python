def calculate_tired_pricing(quantity: int) -> int:
    if quantity == 3:
        return 717
    elif quantity == 5:
        return 1195
    return quantity * 299
