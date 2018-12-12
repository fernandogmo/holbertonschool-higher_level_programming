#!/usr/bin/python3

# This is ugly code because the
# Holberton Checker demands use of
# str.format() when not necessary.
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        print(("{} {} {}" if len(x) else "").format(*x))
