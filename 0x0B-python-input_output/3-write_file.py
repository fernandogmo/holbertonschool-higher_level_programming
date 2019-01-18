#!/usr/bin/python3
""" module `3-write_file` provides the `write_file` function """


def write_file(filename="", text=""):
    """ returns the number of chars written to `filename` from `text` """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
