"""
Check out Codely's repository for a full explanation:
    https://github.com/CodelyTV/refactoring-code_smells-design_patterns/tree/de397ea9e331215aa8e5c9ea4e5ff16270a9ba0f/exercises/tiered_pricing
"""

import pytest

from tdd_in_python import calculate_tired_pricing


@pytest.mark.parametrize(
    "quantity,tired_price",
    [
        (1, 299),
        (2, 598),
        (3, 717),
        (4, 956),
        (5, 1195),
        (11, 2409),
        (12, 2628),
        (13, 2847),
        (26, 5174),
        (27, 5373),
        (28, 5572),
        (50, 9950),
        (51, 7599),
    ],
)
def test_calculate_tired_pricing(quantity, tired_price):
    assert calculate_tired_pricing(quantity) == tired_price
