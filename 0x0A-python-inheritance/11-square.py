#!/usr/bin/python3
"""Module 11-square
Creates a Square Class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square
    """

    def __init__(self, size):
        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        return self.__size ** 2
