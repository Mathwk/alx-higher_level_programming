#!/usr/bin/python3
"""
11-student.py
"""


class Student:
    """ student class"""

    def __init__(self, first_name, last_name, age):
        """ constructs a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns json representation"""
        return self.__dict__
