def calculate_graduated_tiered_pricing(number):
    tier_1_price = 299
    tier_1_total = 2 * tier_1_price

    if number >= 51:
        return (
            tier_1_total + (8 * 239) + (15 * 219) + (25 * 199) + ((number - 50) * 149)
        )
    if number >= 26:
        return tier_1_total + (8 * 239) + (15 * 219) + ((number - 25) * 199)
    if number >= 11:
        return tier_1_total + (8 * 239) + ((number - 10) * 219)
    if number >= 3:
        return tier_1_total + ((number - 2) * 239)
    return number * tier_1_price
