#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = {}
    for x in a_dictionary:
        n_dictionary[x] = a_dictionary[x] * 2
    return n_dictionary
