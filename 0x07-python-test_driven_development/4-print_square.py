#!/usr/bin/python3
"""
This is the "4-print_square" module
for the Holberton School Higher Level Programming track.

The 4-print_square module supplies one function, matrix_divided().
For example,

>>> print_square(4)
####
####
####
####

"""


def print_square(size):
    """ Prints a square made with the char `#`. """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size > 0:
        print(('#' * size + '\n') * size, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
