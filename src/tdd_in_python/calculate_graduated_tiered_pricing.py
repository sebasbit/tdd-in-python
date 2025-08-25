def calculate_graduated_tiered_pricing(number):
    if number >= 3:
        return 2 * 299 + ((number - 2) * 239)
    return number * 299
