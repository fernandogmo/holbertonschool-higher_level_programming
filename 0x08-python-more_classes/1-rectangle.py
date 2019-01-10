#!/usr/bin/python3
"""
Defines a `Rectangle` class
"""


class Rectangle:
    """ a `Rectangle` class """

    def __init__(self, width=0, height=0):
        """ Initializes private instance attributes
            `__height` and `__height`. """
        self.__check_width(width)
        self.__check_height(height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for `__width` """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for `__width` """
        self.__check_width(value)
        self.__width = value

    @property
    def height(self):
        """ getter for `__height` """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for `__height` """
        self.__check_height(value)
        self.__height = value

    @staticmethod
    def __check_width(width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @staticmethod
    def __check_height(height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
