def calculate_graduated_tiered_pricing(number):
    if number >= 11:
        return (2 * 299) + (8 * 239) + ((number - 10) * 219)
    if number >= 3:
        return 2 * 299 + ((number - 2) * 239)
    return number * 299
