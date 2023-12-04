#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for rows in range(len(matrix)):
            for col in range(len(matrix[rows])):
                if col != len(matrix[rows]) - 1:
                    space = ' '
                else:
                    space = ''
                print("{:d}".format(matrix[rows][col]),end=space)
            print()
