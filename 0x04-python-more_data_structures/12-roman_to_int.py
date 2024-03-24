#!/usr/bin/python3
def roman_to_int(roman_str):
    """ converts a Roman numeral to an integer."""
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_str is None) or (type(roman_str) is not str):
        return 0

    roman_length = len(roman_str)
    value_int = roman_dict[roman_str[roman_length - 1]]
    for i in range(roman_length - 1, 0, -1):
        current_val = roman_dict[roman_str[i]]
        prev_val = roman_dict[roman_str[i - 1]]

        if prev_val >= current_val:
            value_int += prev_val
        else:
            value_int -= prev_val

    return value_int
