#!/usr/bin/python3
"""
This is the "2-matrix_divided" module
for the Holberton School Higher Level Programming track.

The 2-matrix_divided module supplies one function, matrix_divided().
For example,

>>> matrix = [     # doctest: +ELLIPSIS
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> print(matrix_divided(matrix, 3)) # doctest: +NORMALIZE_WHITESPACE
[[0.33, 0.67, 1.0],
 [1.33, 1.67, 2.0]]

>>> print(matrix) # doctest: +NORMALIZE_WHITESPACE
[[1, 2, 3],
 [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """ Returns matrix with all numerical values divided by div. """

    # check matrix is list of lists
    BAD_MATRIX = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or any(map(lambda _: type(_) != list, matrix)):
        raise TypeError(BAD_MATRIX)

    # check div is integer or float, not zero
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check all rows are same length
    if min(matrix, key=len) != max(matrix, key=len):
        raise TypeError("Each row of the matrix must have the same size")

    # check all elements are integer or float
    for row in matrix:
        if any(map(lambda _: type(_) not in (int, float), row)):
            raise TypeError(BAD_MATRIX)

    return [[round(i / div, 2) for i in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
