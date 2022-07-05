#!/usr/bin/python3
"""
Module 12-pascal_triangle
Returns a list of integers representing pascals' triangle
"""


def pascal_triangle(n):
    """Creates the pascals' triangle"""
    pt = []
    fn = []
    for i in range(n):
        nt = [1] + [sum(fn[elem:elem + 2]) for elem in range(len(fn) - 1)]
        if i > 0:
            nt = nt + [1]
        pt.append(nt)
        fn = nt
    return pt
