#!/usr/bin/python3
"""
12-student.py
"""


class Student:
    """ student class"""

    def __init__(self, first_name, last_name, age):
        """ constructs a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns json representation"""
        if type(attrs) == list and all(type(item) == str for item in attrs):
            d = {}
            for i in attrs:
                if i in self.__dict__:
                    d[i] = self.__dict__[i]
            return d
        return self.__dict__
