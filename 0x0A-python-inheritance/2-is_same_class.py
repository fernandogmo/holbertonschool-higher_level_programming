#!/usr/bin/python3
""" module `2-is_same_class` provides the `is_same_class` function """


def is_same_class(obj, a_class):
    """ boolean tests if `obj` is exactly an instance of `a_class` """
    return type(obj) == a_class


if __name__ == '__main__':
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
