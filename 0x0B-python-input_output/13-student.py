#!/usr/bin/python3
""" Module `13-Student provides the `Student` class """


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance
        with specified attributes"""
        if attrs is None or type(attrs) != list:
            return self.__dict__
        d = {}
        for a in attrs:
            if type(a) != str:
                return self.__dict__
            elif a in self.__dict__.keys():
                d[a] = self.__dict__[a]
        return d

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k in json.keys():
            setattr(self, k, json[k])
