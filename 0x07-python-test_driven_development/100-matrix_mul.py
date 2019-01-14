#!/usr/bin/python3
"""
This is the "100-matrix_mul" module
for the Holberton School Higher Level Programming track.

The 100-matrix_mul module supplies one function, matrix_mul.
"""


def matrix_mul(m_a, m_b):
    """ Returns the n x m matrix product of
        an n x p matrix `m_a` and an p x m matrix `m_b`. """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if any(type(_) != list for _ in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(_) != list for _ in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")
    if any(type(_) not in (int, float) for row in m_a for _ in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(type(_) not in (int, float) for row in m_b for _ in row):
        raise TypeError("m_b should contain only integers or floats")
    if min(m_a, key=len) != max(m_a, key=len):
        raise TypeError("each row of m_a must should be of the same size")
    if min(m_b, key=len) != max(m_b, key=len):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    T_b = zip(*m_b)  # Transpose of matrix `m_b`
    return [[sum(ea * eb for ea, eb in zip(a, b)) for b in T_b] for a in m_a]


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
