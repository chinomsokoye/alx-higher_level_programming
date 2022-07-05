#!/usr/bin/python3
"""
Module 1-write_file
Writes a string to a text file
"""


def write_file(filename="", text=""):
    """Write a string to a text file"""
    with open(filename, 'w+') as files:
        return files.write(text)
