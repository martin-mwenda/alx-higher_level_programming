#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    guide = []
    for x in matrix:
        guide.append(list(map(lambda x: x**2, x)))
    return (guide)
