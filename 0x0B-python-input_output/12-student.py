#!/usr/bin/python3
""" Module `12-Student provides the `Student` class """


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

if __name__ == '__main__':
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
