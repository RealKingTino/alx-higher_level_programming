#!/usr/bin/python3
"""Defines a base model class."""


import random
import csv
import turtle
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string.

        Args:
            json_string (str): A JSON string representing a list of dic

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary: A dictionary containing attribute-value pairs.

        Returns:
            object: An instance with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        dict_list = cls.from_json_string(json_string)
        instance_list = [cls.create(**d) for d in dict_list]
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the CSV representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if isinstance(obj, cls):
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    row = [int(value) for value in row]
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        id, width, height, x, y = row
                        list_objs.append(cls(id, width, height, x, y))
                    elif cls.__name__ == "Square" and len(row) == 4:
                        id, size, x, y = row
                        list_objs.append(cls(id, size, x, y))
        except FileNotFoundError:
            return []
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw random shapes with random colors using Turtle graphics."""
        screen = turtle.Screen()
        screen.setup(800, 600)
        screen.title("Artistic Design")

        pen = turtle.Turtle()
        pen.speed(0)

        # Function to set a random color
        def set_random_color():
            colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff']
            pen.fillcolor(random.choice(colors))

        # Function to draw a random shape
        def draw_random_shape(size):
            sides = random.randint(3, 6)
            angle = 360 / sides
            for _ in range(sides):
                pen.forward(size)
                pen.left(angle)

        # Draw rectangles
        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            set_random_color()
            pen.begin_fill()
            draw_random_shape(rect.width)
            pen.end_fill()

        # Draw squares
        for sq in list_squares:
            pen.penup()
            pen.goto(sq.x, sq.y)
            pen.pendown()
            set_random_color()
            pen.begin_fill()
            draw_random_shape(sq.size)
            pen.end_fill()

        turtle.done()

if __name__ == "__main__":
    # Example usage
    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
