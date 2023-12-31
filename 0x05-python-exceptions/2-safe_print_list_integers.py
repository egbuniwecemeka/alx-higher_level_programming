#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
        Print x elements in a list that are integers

        Args:
        my_kist[]: Contains list of vales to check
        x: value to be printed

        Return: x elements
    """
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (num)
