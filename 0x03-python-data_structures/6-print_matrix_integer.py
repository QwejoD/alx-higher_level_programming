#!/usr/bin/python3
'''A function tht prints a matrix of integers'''

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if i.index(j) == len(i) - 1:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
        print()
