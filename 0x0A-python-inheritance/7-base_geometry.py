#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    Base class representing a base geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args:
            name: The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
