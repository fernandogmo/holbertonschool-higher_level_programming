#!/usr/bin/python3
"""
Module `8-base_geometry` provides \
the `BaseGeometry` class and its subclass `Rectangle`
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a `Rectangle` that inherits from `BaseGeometry` """
    def __init__(self, width, height):
        """
        Initializes validated private instace vars \
        `__width` and `__height`
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
