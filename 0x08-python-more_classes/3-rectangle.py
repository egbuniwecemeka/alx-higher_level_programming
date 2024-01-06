#!usr/bin/python3
""" Defines a srectangle """


class Rectangle:
    """ Represents a Rectangle """

    def __init__(self, width=0, height=0):
        """ Initializing Rectangle
            Args:
            width(int): The width of a rectangle
            height(int): The height of a rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets or sets the width of a rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets or sets the height of a rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Sets the area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Sets the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Represents a printable rectangle

            Rectangle is represented by '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
