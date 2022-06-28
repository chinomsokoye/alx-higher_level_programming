#!/usr/bin/python3
"""
Module to import 5-text_indentation
Defines and prints text with new lines (2)
Utilizes a string
"""


def text_indentation(text):
    """Prints text with new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in ".?:":
        text = text.replace(character, character + "\n\n")
        list_lines = [lines.strip(' ') for lines in text.split('\n')]
        revise = "\n".join(list_lines)
        print(revise, end="")
