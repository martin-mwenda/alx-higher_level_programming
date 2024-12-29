#!/usr/bin/python3
"""
This module provides a function to add two numbers.
The function ensures the inputs are integers or floats, casts them to
integers if needed, and returns their sum.
"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as integers

    Args:
        a: first argument (integer or float)
        b: second argument (integer or float, default is 98)

    Returns:
        Sum of the two arguments as an integer.

    Raises:
        TypeError: If either of the arguments is not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
