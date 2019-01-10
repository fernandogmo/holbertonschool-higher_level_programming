#!/usr/bin/python3
"""
Defines a `Rectangle` class
"""


class Rectangle:
    """ a `Rectangle` class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes private instance attributes
            `__height` and `__height`.
            Increases counter of `Rectangle` instances. """
        self.__check_width(width)
        self.__check_height(height)
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """ returns canonical string representation of `Rectangle`
            instance for the developer """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ prints `Bye rectangle...` when instance is deleted,
            and ecreases counter of `Rectangle` instances. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


if __name__ == '__main__':
    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
