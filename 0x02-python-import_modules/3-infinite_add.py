#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_length = len(sys.argv) - 1
    total = 0
    for i in range(argv_length):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
