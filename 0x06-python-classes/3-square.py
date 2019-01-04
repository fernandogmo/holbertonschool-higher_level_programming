#!/usr/bin/python3
class Square:
    """ `Square` class """
    def __init__(self, size=0):
        """ Initializes private instance
            posivive integer `size` """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculates instance area """
        return self.__size ** 2
