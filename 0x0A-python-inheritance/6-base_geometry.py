#!/usr/bin/python3
""" Module base geometry
"""


class BaseGeometry:
    """
    Base class representing a base geometry.
    """
    def area(self):
        """
        Raises Exception: Always raises an exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")
