#!/usr/bin/python3
"""
The `base` module provides the `Base` class for the `models` module.
"""
import json


class Base:
    """
    A `Base` class using a private class attribute `__nb_objects` to
    manage the public instance attribute `id` in all our future classes
    and to avoid duplicating the same code (by extension, same bugs).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes `id` with input value, if given,
        else increment `__nb_objects` and assign its new value to `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string repr
        """
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of jSON string repr
        """
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        return json.loads(json_string)


if __name__ == '__main__':
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
