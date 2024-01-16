#!/usr/bin/python3
""" A Rectangle clas inheriting from Base"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class definition """

    def __init__(self, width, height, x=0, y=0, id=None):

        """
            Initialize a new Rectangle

            Attributes:
            width(int): Width of the new Rectangle
            height(int): Height of new Rectaangle
            x(int): x coordinate of rectangle
            y(int): y coordinate of rectangle
            id(int): identity of Rectangle

            Raises:
            TypeError: If either of width or height is not an int
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Set/Get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets/Sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets/Sets the x coordinate of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets/Sets the y coordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of a rectangle """
        return self.width * self.height

    def display(self):
        """ Prints a rectangle sing '#' character """
        if self.width == 0 or self.height == 0:
            print("")
        return [print("") for y in range(self.y)]
    for h in range(self.height):
        [print(" ", end="") for x in range(self.x)]
        [print("#", end="") for w in range(self.width)]
        print("")

    def update(self, *args, **kwargs):
        """ Updates the rectangle

        Args:

            *args(int): Attributes count list
                1st attr: id
                2nd attr: width
                3rd attr: height
                4th attr: x cord
                5th attr: y cord

            **kwargs(dict): key/value attributes pairs

        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.h)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """ Represents the print() and str(0 representation of a rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
