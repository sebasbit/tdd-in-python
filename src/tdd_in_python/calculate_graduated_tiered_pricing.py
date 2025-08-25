class Tier:
    def __init__(self, max_subs, price):
        self.max_subs = max_subs
        self.price = price

    def total_cost(self):
        return self.max_subs * self.price


def calculate_graduated_tiered_pricing(number):
    tier_1 = Tier(2, 299)

    tier_2_price = 239
    tier_2_total = 8 * tier_2_price

    tier_3_price = 219
    tier_3_total = 15 * tier_3_price

    tier_4_price = 199
    tier_4_total = 25 * tier_4_price

    tier_5_price = 149

    if number >= 51:
        return (
            tier_1.total_cost()
            + tier_2_total
            + tier_3_total
            + tier_4_total
            + ((number - 50) * tier_5_price)
        )
    if number >= 26:
        return (
            tier_1.total_cost()
            + tier_2_total
            + tier_3_total
            + ((number - 25) * tier_4_price)
        )
    if number >= 11:
        return tier_1.total_cost() + tier_2_total + ((number - 10) * tier_3_price)
    if number >= 3:
        return tier_1.total_cost() + ((number - 2) * tier_2_price)
    return number * tier_1.price
