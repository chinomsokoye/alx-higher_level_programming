#!/usr/bin/python3
""" Find a peak from a list of unsorted integers """


def search(low, high, ints):
    """ Defines the search """
    mid = (low + high) // 2
    if low == high:
        return ints[high]
    if ints[mid] < ints[mid + 1]:
        return(search(mid + 1, high, ints))
    return(search(low, mid, ints))


def find_peak(list_of_integers):
    """ Find a peak of list_of_integers """
    if not list_of_integers:
        return
    return(search(0, len(list_of_integers) - 1, list_of_integers))
