#!/usr/bin/python3
"""
This is the "101-matrix_mul" module
for the Holberton School Higher Level Programming track.

The 101-matrix_mul module supplies one function, lazy_matrix_mul.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Uses `NumPy` to return the n x m matrix product of
        an n x p matrix `m_a` and an p x m matrix `m_b`. """
    return np.matmul(m_a, m_b)

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
