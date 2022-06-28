#!/usr/bin/python3
"""
Module to import 100-matrix_mul
Defines matrix multiplication method
Utilizes sized lists, ints and floats rows
"""


def matrix_mul(m_a, m_b):
    """Defines matrix multiplication"""
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("{} must be a list".format
                        ("m_a" if not isinstance(m_a, list) else "m_b"))
    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("{} can't be empty".format
                         ("m_a" if len(m_a) == 0 else "m_b"))

    for eachrow in m_b:
        for n in eachrow:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or float")
        if len(eachrow) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    li = []
    new_matrix = []
    n = 0
    for row_a in range(len(m_a)):
        li = []
        for col_b in range(len(m_b[0])):
            for x in range(len(m_a[0])):
                n += m_a[row_a][x] * m_b[x][col_b]
            li.append(n)
            n = 0
        new_matrix.append(li)
    return new_matrix
