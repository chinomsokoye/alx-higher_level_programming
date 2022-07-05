#!/usr/bin/python3
"""
Module 0-read_file
Reads a file and print to standard output
"""


def read_file(filename=""):
    """Read from filename, Prints to stdout"""
    with open(filename) as f:
        files = f.read()
        print(files, end="")
