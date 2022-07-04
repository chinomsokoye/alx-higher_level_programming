#!/usr/bin/python3
"""Module 10-square
Contains 9-rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square"""

    def __init__(self, size):
        """Initializes the function"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
