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
        """ helper to validate value for `__width` """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @staticmethod
    def __check_height(height):
        """ helper to validate value for `__height` """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ returns string representation of `Rectangle`
            instance for end user """
        if self.area() == 0:
            return ""
        return "\n".join(['#' * self.width] * self.height)


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(
        my_rectangle.area(), my_rectangle.perimeter()))
    print(my_rectangle)
    print(repr(my_rectangle))
    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(
        my_rectangle.area(), my_rectangle.perimeter()))
    print(my_rectangle)
    print(repr(my_rectangle))
