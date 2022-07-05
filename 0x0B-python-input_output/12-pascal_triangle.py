#!/usr/bin/python3
"""
Module 12-pascal_triangle
Returns a list of integers representing pascals' triangle
"""


def pascal_triangle(n):
    """Creates the pascals' triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pt == [[1]]
    for rows in range(n - 1):
        pt.append([x+y for x, y in zip([0] + pt[-1], pt[-1] + [0])])
    return pt
