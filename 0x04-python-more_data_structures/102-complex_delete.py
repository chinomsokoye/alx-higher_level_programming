#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value:
        for key, valu in list(a_dictionary.items()):
            if valu is value:
                del a_dictionary[key]
        return a_dictionary
