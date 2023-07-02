#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""


def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a (int or float): First number.
        b (int or float): Second number. Default value is 98.

    Returns:
        int: The sum of `a` and `b`.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
