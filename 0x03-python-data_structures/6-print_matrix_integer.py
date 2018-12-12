#!/usr/bin/python3

# This is ugly code because the
# Holberton Checker demands use of
# str.format() when not necessary.
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        print(("{:d} {:d} {:d}" if len(x) else "").format(*x))


matrix = [
            [1, 2, 3],
                [4, 5, 6],
                    [7, 8, 9]
                    ]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

