#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square class.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate. Defaults to 0.
            y (int, optional): y-coordinate. Defaults to 0.
            id (int, optional): The ID of the object.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """sets value for height and width"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes.

        Args:
            *args: List of non-keyword arguments.
            **kwargs: Double pointer to a dictionary containing
            keyworded arguments.

        Note:
            Each key in kwargs represents an attribute to update.
        """
        if args and len(args) > 0:
            attribute_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attribute_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
