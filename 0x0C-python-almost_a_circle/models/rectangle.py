#!/usr/bin/python3
"""
The `rectangle` module provides the `Rectangle` class for the `models` module.
"""
from base import Base


class Rectangle(Base):
    """
    A `Rectangle` class inheriting from `Base` and using private instance
    attributes with individual getters and setters.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes `id` using `Base` class `__init__`.
        Initializes `__width`, `__height`, `__x`, and `__y`.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ `__width` getter """
        return self.__width

    @width.setter
    def width(self, v):
        """ `__width` setter """
        self.__width = v

    @property
    def height(self):
        """ `__height` getter """
        return self.__height

    @height.setter
    def height(self, v):
        """ `__height` setter """
        self.__height = v

    @property
    def x(self):
        """ `__x` getter """
        return self.__x

    @x.setter
    def x(self, v):
        """ `__x` setter """
        self.__x = v

    @property
    def y(self):
        """ `__y` getter """
        return self.__y

    @y.setter
    def y(self, v):
        """ `__width` setter """
        self.__y = v

if __name__ == '__main__':
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
