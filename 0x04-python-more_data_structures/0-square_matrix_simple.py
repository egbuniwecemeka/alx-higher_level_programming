#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in matrix:
        square.append([j**2 for j in i])
    return square
