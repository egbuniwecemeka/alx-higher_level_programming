#!/usr/bin/python3
""" A function that adds two integers """


def add_integer(a, b=98):
    """
        Returns the addittion of two integers

        Floats are type casted to integers before addition operation

        Raise:
            A TypeError if a or b is not an integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
