#!/usr/bin/python3
""" module `1-number_of_lines` provides the `number_of_lines` function """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename, 'r', encoding='utf8') as f:
        return sum(1 for line in f)


if __name__ == '__main__':

    filename = "my_file_0.txt"
    nb_lines = number_of_lines(filename)
    print("{} has {:d} lines".format(filename, nb_lines))
