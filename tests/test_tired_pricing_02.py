"""
Check out Codely's repository for a full explanation:
    https://github.com/CodelyTV/refactoring-code_smells-design_patterns/tree/de397ea9e331215aa8e5c9ea4e5ff16270a9ba0f/exercises/tiered_pricing
"""

from tdd_in_python import calculate_tired_pricing


def test_calculate_tired_pricing_for_range_1_to_2():
    assert calculate_tired_pricing(1) == 299
    assert calculate_tired_pricing(2) == 598


def test_calculate_tired_pricing_for_range_3_to_10():
    assert calculate_tired_pricing(3) == 717
    assert calculate_tired_pricing(5) == 1195
