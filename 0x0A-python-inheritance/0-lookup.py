#!/usr/bin/python3
"""  returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    A list of strings containing the names of attributes and methods.

    """
    return dir(obj)
