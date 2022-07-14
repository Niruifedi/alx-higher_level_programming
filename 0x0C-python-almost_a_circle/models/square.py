#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherits from the
        super class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getting property of atrributes"""
        return(self.width)

    @size.setter
    def size(self, value):
        """set value of attribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
        return self.size

    def update(self, *args, **kwargs):
        """no word arguments and key word arguments"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """returns dictionary representation of Square"""
        return {
            'id': getattr(self, 'id'),
            'x': getattr(self, 'x'),
            'size': getattr(self, 'size'),
            'y': getattr(self, 'y')
        }

    def __str__(self):
        """string overloading method"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
