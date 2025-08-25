class Tier:
    def __init__(self, min_subs: int, max_subs: int, price: int) -> None:
        self.min_subs = min_subs
        self.max_subs = max_subs
        self.price = price

    def apply_for(self, n_subs: int) -> bool:
        return self.min_subs <= n_subs

    def cost_for(self, n_subs: int) -> int:
        if n_subs < self.min_subs:
            return 0
        if n_subs > self.max_subs:
            return self.price * self.total_subs_in_tier()
        return self.price * self.subs_in_tier(n_subs)

    def subs_in_tier(self, n_subs: int) -> int:
        return n_subs - self.min_subs + 1

    def total_subs_in_tier(self) -> int:
        total_subs_in_tier = self.max_subs - self.min_subs + 1
        return total_subs_in_tier


def calculate_graduated_tiered_pricing(subscriptions: int) -> int:
    tiers = (
        Tier(1, 2, 299),
        Tier(3, 10, 239),
        Tier(11, 25, 219),
        Tier(26, 50, 199),
        Tier(51, 999, 149),
    )

    total_price = 0
    for tier in tiers:
        if tier.apply_for(subscriptions):
            total_price += tier.cost_for(subscriptions)
        else:
            break

    return total_price
