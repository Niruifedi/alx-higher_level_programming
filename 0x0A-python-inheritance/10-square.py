#!/usr/bin/python3

"""import rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implent a square"""
    def __init__(self, size):
        """size of square"""
        self.__size = size
        super().__init__(self.__size, self.__size)
