#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes an element at a specified index in the list.

    Args:
        my_list (list): A list of elements. Defaults to an empty list.
        idx (int): The index of the element to be deleted. Defaults to 0.

    Returns:
        list: The list after the specified element is deleted, or the
              original list if the index is out of range.
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
