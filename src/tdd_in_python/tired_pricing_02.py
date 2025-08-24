def calculate_tired_pricing(quantity: int) -> int:
    if 3 <= quantity <= 10:
        return quantity * 239
    elif 11 <= quantity <= 25:
        return quantity * 219
    elif 26 <= quantity <= 50:
        return quantity * 199
    elif quantity > 50:
        return quantity * 149
    return quantity * 299
