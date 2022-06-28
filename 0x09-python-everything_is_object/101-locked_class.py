#!/usr/bin/python3
"""Import module 101-locked_class
Defines class with no object attribute
"""


class LockedClass():
    """Defines a class
    Prevents new instance been created dynamically
    Unless first_name
    >>> a = LockedClass()
    >>> a.first_name = 'Chinomso'
    >>> a.first_name
    'Chinomso
    >>> a.last_name = 'Ok'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
