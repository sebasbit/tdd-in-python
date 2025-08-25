"""
Check out Codely's repository for a full explanation:
    https://github.com/CodelyTV/refactoring-code_smells-design_patterns/tree/de397ea9e331215aa8e5c9ea4e5ff16270a9ba0f/exercises/graduated_tiered_prices
"""

from tdd_in_python import calculate_graduated_tiered_pricing


def test_calculate_graduated_tiered_pricing_for_1_sub():
    assert calculate_graduated_tiered_pricing(1) == 299


def test_calculate_graduated_tiered_pricing_for_2_subs():
    assert calculate_graduated_tiered_pricing(2) == 598
