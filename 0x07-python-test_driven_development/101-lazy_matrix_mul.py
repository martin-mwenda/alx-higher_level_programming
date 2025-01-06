#!/usr/bin/python3
""" lazy_matrix_mul module """

import numpy as np


def lazy_matrix_mul(prmMatrixA, prmMatrixB):
    """
    Multiplies two matrices lazily.

    This function performs matrix multiplication without immediately
    calculating all values. Instead, it returns a generator that yields
    the result row-by-row. This can be beneficial for very large matrices
    where calculating the entire product at once might
    consume excessive memory.

    Args:
        prmMatrixA: The first matrix.
        prmMatrixB: The second matrix.

    Yields:
        A row of the resulting matrix.

    Raises:
        TypeError: If either prmMatrixA or prmMatrixB is not a list of lists.
        TypeError: If either prmMatrixA or prmMatrixB is empty.
        TypeError: If an element in either matrix is not a number.
        ValueError: If the number of columns in prmMatrixA does not match
                     the number of rows in prmMatrixB.

    """
    if prmMatrixA is None:
        raise TypeError("m_a should be indicate")
    if prmMatrixB is None:
        raise TypeError("m_b should be indicate")
    if not isinstance(prmMatrixA, list):
        raise TypeError("m_a must be a list")
    if not isinstance(prmMatrixB, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(ele, list) for ele in prmMatrixA):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in prmMatrixB):
        raise TypeError("m_b must be a list of lists")
    if len(prmMatrixA) == 0 or len(prmMatrixA[0]) == 0:
        raise TypeError("m_a can't be empty")
    if len(prmMatrixB) == 0 or len(prmMatrixB[0]) == 0:
        raise TypeError("m_b can't be empty")

    arr1 = np.array(prmMatrixA)
    arr2 = np.array(prmMatrixB)
    return np.matmul(arr1, arr2)
