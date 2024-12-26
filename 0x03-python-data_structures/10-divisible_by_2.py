def divisible_by_2(my_list=[]):
    """
    Checks if each integer in the list is divisible by 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of booleans, where True indicates that the integer at
              that position is divisible by 2, and False otherwise.
    """
     new = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return (new)
