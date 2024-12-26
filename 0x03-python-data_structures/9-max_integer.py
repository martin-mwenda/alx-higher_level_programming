def max_integer(my_list):
    """
    Returns the maximum integer from a list of integers.

    Args:
        my_list (list): A list of integers.

    Returns:
        int: The maximum integer in the list. If list is empty, returns None.
    """
    if len(my_list) == 0:
        return (None)
    max_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]
    return (max_num)
