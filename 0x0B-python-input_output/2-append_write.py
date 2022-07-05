#!/usr/bin/python3
"""
Module 2-append_write
Append to text file, returns number of characters added
"""


def append_write(filename="", text=""):
    """Appends to text file, returns number of characters added"""
    with open(filename, 'a+') as files:
        return files.write(text)
