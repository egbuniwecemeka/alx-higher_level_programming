#!/usr/bin/python3
def safe_print_integer(value):
    """
        Prints an integer {:d}.format

        Args:
            (value)an integer

        Return:
            If TypeError or ValueError - False
            Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
