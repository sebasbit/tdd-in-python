class Tier:
    def __init__(self, min_subs, max_subs, price):
        self.min_subs = min_subs
        self.max_subs = max_subs
        self.price = price

    def apply(self, n_subs):
        return self.min_subs <= n_subs <= self.max_subs

    def cost_of(self, n_subs):
        return self.price * (n_subs - self.min_subs + 1)

    def total_cost(self):
        return (self.max_subs - self.min_subs + 1) * self.price


def calculate_graduated_tiered_pricing(number):
    tier_1 = Tier(1, 2, 299)
    tier_2 = Tier(3, 10, 239)
    tier_3 = Tier(11, 25, 219)
    tier_4 = Tier(26, 50, 199)
    tier_5 = Tier(51, 999, 149)

    if tier_5.apply(number):
        return (
            tier_1.total_cost()
            + tier_2.total_cost()
            + tier_3.total_cost()
            + tier_4.total_cost()
            + tier_5.cost_of(number)
        )
    if tier_4.apply(number):
        return (
            tier_1.total_cost()
            + tier_2.total_cost()
            + tier_3.total_cost()
            + tier_4.cost_of(number)
        )
    if tier_3.apply(number):
        return tier_1.total_cost() + tier_2.total_cost() + tier_3.cost_of(number)
    if tier_2.apply(number):
        return tier_1.total_cost() + tier_2.cost_of(number)
    return tier_1.cost_of(number)
