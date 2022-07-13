#!/usr/bin/python3
"""first Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from
        Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id=id)

    @property
    def width(self):
        """get attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of attribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        return self.__width

    @property
    def height(self):
        """get attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of attribute"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value
        return self.__height

    @property
    def x(self):
        """get attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """set value of attribute"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value
        return self.__x

    @property
    def y(self):
        """get attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """set value of attribute"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
        return self.__y

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle representation"""
        [print() for i in range(self.__y)]
        for j in range(self.__height):
            [print(" ", end='') for i in range(self.__x)]
            for w in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """no word arguments and key word arguments"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        else:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns dictionary representation of Rectangle."""
        return {'x': getattr(self, 'x'),
                'y': getattr(self, 'y'),
                'id': getattr(self, 'id'),
                'width': getattr(self, 'width'),
                'height': getattr(self, 'height')
                }

    def __str__(self):
        """string overloading method"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
