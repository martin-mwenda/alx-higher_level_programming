#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise. If a tuple has less than 2 elements,
    zeros are assumed for missing elements.

    Args:
        tuple_a (tuple): The first tuple. Defaults to ().
        tuple_b (tuple): The second tuple. Defaults to ().

    Returns:
        tuple: A tuple containing the sum of corresponding elements from
               tuple_a and tuple_b.
    """
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
