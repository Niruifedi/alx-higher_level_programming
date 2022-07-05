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
