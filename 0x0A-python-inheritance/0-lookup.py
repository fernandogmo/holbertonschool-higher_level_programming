#!/usr/bin/python3
""" module `0-lookup` contains the `lookup` function """


def lookup(obj):
    """ returns the list of of available attributes and methods for `obj` """
    return dir(obj)


if __name__ == '__main__':
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

    def my_meth(self):
        pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
