#!/usr/bin/python3
"""
@author: Aliyu Adekola
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        str funtion to print with/height

        Returns:
            Return width/height
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
