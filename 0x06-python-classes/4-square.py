#!/usr/bin/python3
""" A Square class """


class Square:
    """ Creates a square """

    def __init__(self, size=0):
        """ Initializes a new Square class

        Args:
            size (int): Size of square
        """
        self.__size = size

    @property
    def size(self):
        """ Get/size current size of square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ current area square """
        return (self.__size * self.__size)
