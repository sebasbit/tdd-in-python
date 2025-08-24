"""
Check out Codely's repository for a full explanation:
    https://github.com/CodelyTV/refactoring-code_smells-design_patterns/tree/de397ea9e331215aa8e5c9ea4e5ff16270a9ba0f/exercises/tiered_pricing
"""

from tdd_in_python import calculate_tired_pricing


def test_calculate_tired_pricing():
    assert calculate_tired_pricing(1) == 299
