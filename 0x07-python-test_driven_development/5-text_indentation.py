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
        text = text.replace(c, c+"\n")
    lines = list(map(lambda _: _.strip(), text.split("\n")))
    print(*filter(lambda _: len(_) > 0, lines), sep="\n\n")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
