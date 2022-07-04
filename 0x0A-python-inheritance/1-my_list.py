#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
Inherits from MyList class, method to print sorted
"""


class MyList(list):
    """Inherits from list
    Methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """Prints int list sorted in ascending"""
        print(sorted(self))
