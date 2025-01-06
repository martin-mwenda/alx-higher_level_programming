#!/usr/bin/python3
""" matrix_mul module """


def matrix_mul(prmMatrixA, prmMatrixB):
    """
    Multiplies two matrices.

    Args:
        prmMatrixA: The first matrix.
        prmMatrixB: The second matrix.

    Returns:
        The product of the two matrices.

    Raises:
        TypeError: If either prmMatrixA or prmMatrixB is not a list of lists.
        TypeError: If either prmMatrixA or prmMatrixB is empty.
        TypeError: If an element in either matrix is not a number.
        ValueError: If the number of columns in prmMatrixA does not match
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

    columnLenA = len(prmMatrixA[0])

    for row in range(len(prmMatrixA)):
        if len(prmMatrixA[row]) != columnLenA:
            raise TypeError("each row of m_a must be of the same size")

    columnLenB = len(prmMatrixB[0])

    for row in range(len(prmMatrixB)):
        if len(prmMatrixB[row]) != columnLenB:
            raise TypeError("each row of m_b must be of the same size")

    # initialize result matrix
    result = [
        [0 for x in range(len(prmMatrixA[0]))] for y in range(len(prmMatrixA))
        ]

    # iterate through rows of prmMatrixA
    for i in range(len(prmMatrixA)):
        # iterate through columns of prmMatrixB
        for j in range(len(prmMatrixB[0])):
            # iterate through rows of prmMatrixB
            for k in range(len(prmMatrixB)):
                result[i][j] += prmMatrixA[i][k] * prmMatrixB[k][j]

    return result
