#!/usr/bin/python3
""" module `4-inherits_from` provides the `inherits_from` function """


def inherits_from(obj, a_class):
    """ boolean tests `obj` for inheritance from `a_class` """
    return isinstance(obj, a_class) and type(obj) != a_class


if __name__ == '__main__':
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, float):
        print("{} inherited from class {}".format(a, float.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
