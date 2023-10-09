#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for r in range(len(matrix)):
            for item in range(len(matrix[r])):
                if item != len(matrix[r]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[r][item]), end=endspace)
            print()
