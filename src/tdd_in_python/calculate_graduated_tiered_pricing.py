def calculate_graduated_tiered_pricing(number):
    tier_1_price = 299
    tier_1_total = 2 * tier_1_price

    tier_2_price = 239
    tier_2_total = 8 * tier_2_price

    tier_3_price = 219
    tier_3_total = 15 * tier_3_price

    tier_4_price = 199
    tier_4_total = 25 * tier_4_price

    if number >= 51:
        return (
            tier_1_total
            + tier_2_total
            + tier_3_total
            + tier_4_total
            + ((number - 50) * 149)
        )
    if number >= 26:
        return (
            tier_1_total + tier_2_total + tier_3_total + ((number - 25) * tier_4_price)
        )
    if number >= 11:
        return tier_1_total + tier_2_total + ((number - 10) * tier_3_price)
    if number >= 3:
        return tier_1_total + ((number - 2) * tier_2_price)
    return number * tier_1_price
