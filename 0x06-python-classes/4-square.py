#!/usr/bin/python3
""" Square class create """


class Square:
    """ define square """
    def __init__(self, size=0):
        """ initialize new attribute
        arg: size(int)
        """
        self.size = size

    @property
    def size(self):
        """ returns the size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ sets the valuse of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ defines are that return the result """
        return (self.__size * self.__size)
