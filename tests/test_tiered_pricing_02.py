"""
Check out Codely's repository for a full explanation:
    https://github.com/CodelyTV/refactoring-code_smells-design_patterns/tree/de397ea9e331215aa8e5c9ea4e5ff16270a9ba0f/exercises/tiered_pricing
"""

import pytest

from tdd_in_python import calculate_tiered_pricing


@pytest.mark.parametrize(
    "quantity,tired_price",
    [
        (1, 299),
        (2, 598),
        (3, 717),
        (10, 2390),
        (11, 2409),
        (25, 5475),
        (26, 5174),
        (50, 9950),
        (51, 7599),
        (52, 7748),
    ],
)
def test_calculate_tiered_pricing(quantity, tired_price):
    assert calculate_tiered_pricing(quantity) == tired_price


def test_number_of_subscriptions_cannot_be_less_than_one():
    with pytest.raises(ValueError):
        calculate_tiered_pricing(0)
    with pytest.raises(ValueError):
        calculate_tiered_pricing(-1)
