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
    # Ensure both tuples are at least 2 elements long by padding with (0, 0)
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)

    # Add corresponding elements
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]

    return new_tuple
