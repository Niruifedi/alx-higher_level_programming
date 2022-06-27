#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.
        Args:
            width (int): the width of a rectangle
            height (int): the height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
