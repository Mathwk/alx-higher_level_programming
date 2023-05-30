#!/usr/bin/python3
""" Square class create """


class Square:
    def __init__(self, size=0):
        """ define square """
        self.size = size

    @property
    def size(self):
        """ gets the size and returns """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ sets the size to int """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ defines area that returns result """
        return (self.__size * self.__size)

    def my_print(self):
        """ define an out put/ dispay"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
