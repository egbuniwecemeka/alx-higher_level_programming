#!/usr/bin/python3
""" A Square class for size validation """


class Square:
    """ A Square class """

    def __init__(self, size=0):
        """Initialize a new class

        Args:
            size(int): Size of square
        """
        if isinstance(self, size):
            raise TypeError("must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
