#!/usr/bin/python3
""" prints the number and its list of argument """
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments".format(count))
    elif count == 1:
        print("{} argument".format(count))
    else:
        print("{} arguments".format(count))
