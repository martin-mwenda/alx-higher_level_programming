#!/usr/bin/python3


"""Defines a base model class."""

import json
import csv
import turtle


class Base:
    """
    Base class for managing 'id' attribute in future classes.
    """

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.
        Args:
            id (int): The ID of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Shape:
  """Represents a generic geometric shape."""

  def __init__(self, size, x, y):
    self.size = size
    self.x = x
    self.y = y

  def to_dictionary(self):
    """Converts the shape to a dictionary."""
    return {"size": self.size, "x": self.x, "y": self.y}


class Rectangle(Shape):
  """Represents a rectangle."""

  def __init__(self, width, height, x, y):
    super().__init__(size=(width, height), x=x, y=y)

  @staticmethod
  def to_json_string(list_dictionaries):
    """Return the JSON serialization of a list of dictionaries.

    Args:
      list_dictionaries (list): A list of dictionaries.

    Returns:
      str: The JSON serialization of the list of dictionaries.
    """

    if list_dictionaries is None or list_dictionaries == []:
      return "[]"
    return json.dumps(list_dictionaries)

  @classmethod
  def save_to_file(cls, list_objs):
    """Write the JSON serialization of a list of objects to a file.

    Args:
      list_objs (list): A list of Rectangle instances.
    """

    filename = cls.__name__ + ".json"
    with open(filename, "w") as jsonfile:
      if list_objs is None:
        jsonfile.write("[]")
      else:
        list_dicts = [o.to_dictionary() for o in list_objs]
        jsonfile.write(Rectangle.to_json_string(list_dicts))

  @staticmethod
  def from_json_string(json_string):
    """Return the deserialization of a JSON string.

    Args:
      json_string (str): A JSON str representation of a list of dicts.

    Returns:
      list: If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
    """

    if json_string is None or json_string == "[]":
      return []
    return json.loads(json_string)

  @classmethod
  def create(cls, **dictionary):
    """Return a Rectangle instance instantiated from a dictionary of attributes.

    Args:
      **dictionary (dict): Key/value pairs of attributes to initialize.

    Returns:
      Rectangle: A new Rectangle instance.
    """

    if dictionary and dictionary != {}:
      return cls(width=dictionary.get("width", 1), height=dictionary.get("height", 1), **dictionary)

  @classmethod
  def load_from_file(cls):
    """Return a list of Rectangle instances instantiated from a file of JSON strings.

    Reads from `<cls.__name__>.json`.

    Returns:
      list: If the file does not exist - an empty list.
            Otherwise - a list of instantiated Rectangle classes.
    """

    filename = str(cls.__name__) + ".json"
    try:
      with open(filename, "r") as jsonfile:
        list_dicts = Rectangle.from_json_string(jsonfile.read())
        return [cls.create(**d) for d in list_dicts]
    except IOError:
      return []

  @classmethod
  def save_to_file_csv(cls, list_objs):
    """Write the CSV serialization of a list of objects to a file.

    Args:
      list_objs (list): A list of Rectangle instances.
    """

    filename = cls.__name__ + ".csv"
    with open(filename, "w", newline="") as csvfile:
      if list_objs is None or list_objs == []:
        csvfile.write("[]")
      else:
        fieldnames = ["id", "width", "height", "x", "y"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for obj in list_objs:
          writer.writerow(obj.to_dictionary())

  @classmethod
  def load_from_file_csv(cls):
    """Return a list of Rectangle instances instantiated from a CSV file.

    Reads from `<cls.__name__>.csv`.

    Returns:
      list: If the file does not exist - an empty list.
            Otherwise - a list of instantiated Rectangle
    """

    filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
