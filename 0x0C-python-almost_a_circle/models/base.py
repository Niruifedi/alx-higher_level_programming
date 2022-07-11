#!/usr/bin/python3
"""Base Class."""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation constructor
            id: can only accept integer value
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
