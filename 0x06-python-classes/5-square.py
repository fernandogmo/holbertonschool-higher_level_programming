#!/usr/bin/python3
class Square:
    """ `Square` class """
    def __init__(self, size=0):
        """ Initializes private instance
            posivive integer `size` """
        self.__size = size

    @property
    def size(self):
        """ getter for `__size` """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for `__size` """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates instance area """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with `#`s.
            Should probably be a `__repr__`. """
        row = ('#' * self.__size) + '\n'
        if self.__size > 0:
            print(row * self.__size, end="")
        else:
            print()
