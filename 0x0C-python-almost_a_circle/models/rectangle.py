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
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__width = v

    @property
    def height(self):
        """ `__height` getter """
        return self.__height

    @height.setter
    def height(self, v):
        """ `__height` setter """
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__height = v

    @property
    def x(self):
        """ `__x` getter """
        return self.__x

    @x.setter
    def x(self, v):
        """ `__x` setter """
        if type(v) is not int:
            raise TypeError("x must be an integer")
        if v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        """ `__y` getter """
        return self.__y

    @y.setter
    def y(self, v):
        """ `__width` setter """
        if type(v) is not int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v

    def area(self):
        """ Calculates area of rectangle """
        return self.width * self.height

    def display(self):
        """ Displays rectangle using `#` character """

        for row in range(self.y):
            print()
        for row in range(self.height):
            print('{}{}'.format(' ' * self.x, '#' * self.width))

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d


if __name__ == '__main__':
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
