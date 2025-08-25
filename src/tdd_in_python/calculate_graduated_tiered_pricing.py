class Tier:
    def __init__(self, min_subs, max_subs, price):
        self.min_subs = min_subs
        self.max_subs = max_subs
        self.price = price

    def apply(self, n_subs):
        return self.min_subs <= n_subs

    def cost_of(self, n_subs):
        if n_subs < self.min_subs:
            return 0
        if n_subs > self.max_subs:
            return self.total_cost()
        return self.price * (n_subs - self.min_subs + 1)

    def total_cost(self):
        return (self.max_subs - self.min_subs + 1) * self.price


def calculate_graduated_tiered_pricing(number):
    tiers = (
        Tier(1, 2, 299),
        Tier(3, 10, 239),
        Tier(11, 25, 219),
        Tier(26, 50, 199),
        Tier(51, 999, 149),
    )

    total_price = 0
    for tier in tiers:
        if tier.apply(number):
            total_price += tier.cost_of(number)
        else:
            break

    return total_price
