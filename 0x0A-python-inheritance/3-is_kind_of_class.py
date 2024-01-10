#!/usr/bin/python3
""" Define an object-instance and class inherited function """


def is_kind_of_class(obj, a_class):
    """ Checks if an object is an instance of an inherited class

        Args:
        obj: The object that will be check
        a_class: The class to compare it to

        Return:
        Returns true if obj its an instance of inherited class
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
