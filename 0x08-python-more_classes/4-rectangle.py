#!/usr/bin/python3
""" Defines a Rectangle """


class Rectangle:
    """ Represents a rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes Rectangle 
            Args:

            width(int): The width of the rectangle
            height(int): The height of the rectangle

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
        """ Returns the area of a rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Printable representation of a rectangle
            
            Rectangle will be represented by '#'

        """
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
       """ string representation of a rectangle """
       rect = "Rectangle(" + str(self.__width)
       rect += ", " + str(self.__height) + ")"
       return (rect)
