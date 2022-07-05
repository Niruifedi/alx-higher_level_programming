#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """define geometry area"""
    def area(self):
        """no defined area of geometry"""
        raise Exception("area() is not implemented")
