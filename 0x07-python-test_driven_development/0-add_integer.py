#!/usr/bin/python3
"""
This is the "0-add_integer" module
for the Holberton School Higher Level Programming track.

The 0-add_integer module supplies one function, add_integer(). For example,

>>> add_integer(13, 29)
42
"""


def add_integer(a, b=98):
    """ Returns the sum of two int/float parameters. """
    if not type(a) == int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not type(b) == int:
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
