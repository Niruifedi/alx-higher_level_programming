#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """define geometry area"""
    def area(self):
        """no defined area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """methods validates integer values"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
