#!/usr/bin/python3
""" Defines a class that inherits from a list """


class MyList(list):
    """ Class printing in sorted order from a list """

    def print_sorted(self):
        """ Prints list in sorted order """
        print(sorted(self))
