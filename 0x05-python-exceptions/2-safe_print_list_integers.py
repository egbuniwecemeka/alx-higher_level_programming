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
    for i in (0, x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (num)
