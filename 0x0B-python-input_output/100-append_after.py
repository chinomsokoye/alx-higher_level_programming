#!/usr/bin/python3
"""
Module 100-append_after
Inserts a line of text to a file
Aafter each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Append new_string after the search_string"""
    with open(filename, 'r') as files:
        text_str = files.readlines()

    with open(filename, 'w') as f:
        st = ""
        for line in text_str:
            st += line
            if search_string in line:
                st += new_string
        f.write(st)
