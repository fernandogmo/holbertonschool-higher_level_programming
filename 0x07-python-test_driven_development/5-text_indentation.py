#!/usr/bin/python3
"""
This is the "5-text_indentation" module
for the Holberton School Higher Level Programming track.

The 5-text_indentation module supplies one function, matrix_divided().

"""


def text_indentation(text):
    """ Prints a text with 2 new lines after
        each of these characters: ., ? and : """

    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.replace('\n', ' ')
    for c in ".:?":
        text = text.replace(c, c+"\n\n")
    lines = (ln.strip() for ln in text.split("\n"))
    print(*lines, sep="\n", end='')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
