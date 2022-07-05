#!/usr/bin/python3
"""
Module 12-pascal_triangle
Returns a list of integers representing pascals' triangle
"""


def pascal_triangle(n):
    """Creates the pascals' triangle"""
    if n <= 0:
        return []
    ls = [[0 for i in range(x + 1)] for x in range(n)]
    ls[0] = [1]

    for x in range(1, n):
        ls[x][0] = 1
        for y in range(1, x + 1):
            if y < len(ls[x - 1]):
                ls[x][y] = ls[x - 1][y - 1] + 1[x - 1][y]
            else:
                ls[x][y] = ls[x - 1][0]
    return 1
