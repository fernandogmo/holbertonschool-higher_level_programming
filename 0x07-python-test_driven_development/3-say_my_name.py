#!/usr/bin/python3
"""
This is the "3-say_my_name" module
for the Holberton School Higher Level Programming track.

The 3-say_my_name module supplies one function, matrix_divided().
For example,

>>> say_my_name("Bertrand", "Russell")
My name is Bertrand Russell

"""


def say_my_name(first_name, last_name=""):
    """ Prints My name is <first name> <last name>. """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
