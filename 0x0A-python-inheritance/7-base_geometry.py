#!/usr/bin/python3
""" A Base Geometry class integer validator """


class BaseGeometry:
    """ Integer class validation definition """

    def area(self):
        """ Non - functional method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates parameters as integers

            Args:
            name(str): The name of the integer
            value(int):The value of the parameter

            Raises:
            TypeError: Returns error if param is not integer
            ValueError: Returns error if value is less than or 0

        """

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
