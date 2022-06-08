#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        return (dict((a, b*2) for a, b in a_dictionary.items()))
