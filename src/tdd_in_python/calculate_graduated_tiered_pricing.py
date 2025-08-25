def calculate_graduated_tiered_pricing(number):
    tier_1_price = 299
    tier_1_total = 2 * tier_1_price

    tier_2_price = 239
    tier_2_total = 8 * tier_2_price

    if number >= 51:
        return (
            tier_1_total
            + tier_2_total
            + (15 * 219)
            + (25 * 199)
            + ((number - 50) * 149)
        )
    if number >= 26:
        return tier_1_total + tier_2_total + (15 * 219) + ((number - 25) * 199)
    if number >= 11:
        return tier_1_total + tier_2_total + ((number - 10) * 219)
    if number >= 3:
        return tier_1_total + ((number - 2) * tier_2_price)
    return number * tier_1_price
