#!/usr/bin/python3
""" A object-instance-class defining function """


def is_same_class(obj, a_class):
    """ Checks if an object is exactly a class instance 

        Args:
        obj: Object to check
        a_class: class to be compared to

        Return:
        If object and class matches return true
        Otherwise - False
    """

    if type(obj) == a_class:
        return True
    return False
