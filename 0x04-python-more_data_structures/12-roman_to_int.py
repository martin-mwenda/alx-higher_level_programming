#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    total = 0

    for char in roman_string[::-1]:
        current_value = roman_dict.get(char)
        if current_value is None:
            return 0

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

            prev_value = current_value

            return total
