#!/usr/bin/python3


"""Defines a base model class."""


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
