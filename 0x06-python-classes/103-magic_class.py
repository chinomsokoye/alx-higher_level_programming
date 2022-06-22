#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """Initializes and define methods."""
    def __init__(self, radius=0):
        """IInitializes class MagicClass."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius muct be a number")
        self.__radius = radius

    def area(self):
        """Computes area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference."""
        return 2 * math.pi * self.__radius
