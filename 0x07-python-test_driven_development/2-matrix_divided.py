#!/usr/bin/python3
"""
Module 2-matrix_divided
Divides all element of a matrix
Require same list size
"""


def matrix_divided(matrix, div):
    """Return new matrix with divided value"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(res)

    new_matrix = []
    len_matrix = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(res)
        if len(lists) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for x in lists:
            if not isinstance(x, (int, float)):
                raise TypeError(res)
            new_list.append(round(x/div, 2))
        new_matrix.append(new_list)
    return new_matrix
