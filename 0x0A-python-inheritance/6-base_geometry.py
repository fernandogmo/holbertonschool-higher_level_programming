#!/usr/bin/python3
""" module `6-base_geometry` provides the `BaseGeometry` class """


class BaseGeometry:
    """ `BaseGeometry` class """
    def area(self):
        """ raises `not implemented exception """
        raise Exception("area() is not implemented")


if __name__ == '__main__':

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
