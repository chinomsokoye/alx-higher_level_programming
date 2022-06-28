#!/usr/bin/python3
"""
Module to import 4-print_square
Defines and prints square with #'s
Integer values taken in
"""


def print_square(size):
    """Prints square with #'s with integer size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
