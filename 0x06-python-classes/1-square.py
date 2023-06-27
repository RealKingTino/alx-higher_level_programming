#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The private instance attribute to
            store the size of the square.
        """
        self.__size = size  #: size of the square
