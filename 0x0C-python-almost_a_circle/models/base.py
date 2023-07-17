#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """This class serves as the base for all other classes in the
    project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class.

        Args:
            id (int, optional): The ID of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
