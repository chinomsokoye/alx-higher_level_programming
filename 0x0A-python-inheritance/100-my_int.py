#!/usr/bin/python3
"""
Module 100-my_int
Create a class inherit from int
"""


class MyInt(int):
    """Defines a class MyInt
    Inherit from Int
    """
    def __eq__(self, other):
        """Function equality inequality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Function inequality equality"""
        return super().__eq__(other)
