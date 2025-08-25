class Tier:
    def __init__(self, max_subs, price):
        self.max_subs = max_subs
        self.price = price

    def total_cost(self):
        return self.max_subs * self.price


def calculate_graduated_tiered_pricing(number):
    tier_1 = Tier(2, 299)
    tier_2 = Tier(8, 239)
    tier_3 = Tier(15, 219)
    tier_4 = Tier(25, 199)
    tier_5 = Tier(50, 149)

    if number >= 51:
        return (
            tier_1.total_cost()
            + tier_2.total_cost()
            + tier_3.total_cost()
            + tier_4.total_cost()
            + ((number - 50) * tier_5.price)
        )
    if number >= 26:
        return (
            tier_1.total_cost()
            + tier_2.total_cost()
            + tier_3.total_cost()
            + ((number - 25) * tier_4.price)
        )
    if number >= 11:
        return (
            tier_1.total_cost() + tier_2.total_cost() + ((number - 10) * tier_3.price)
        )
    if number >= 3:
        return tier_1.total_cost() + ((number - 2) * tier_2.price)
    return number * tier_1.price
