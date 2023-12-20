#!/usr/bin/python3
""" Area of a square class """

class Square:
    """ Creates a square class """

    def __init__(self, size=0):
        """ Iniitializes a new square

        Args:
            size (int): Size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area of a square """
        return (self.__size * self.__size)
