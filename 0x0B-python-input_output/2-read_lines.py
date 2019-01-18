#!/usr/bin/python3
""" module `2-read_lines` provides the `read_lines` function """


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout """
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            for i, line in enumerate(f):
                if i < nb_lines:
                    print(line, end='')


if __name__ == '__main__':

    print("Full content with -1:")
    read_lines("my_file_0.txt", -1)
    print("--")
    print("3 lines:")
    read_lines("my_file_0.txt", 3)
    print("--")
    print("Full content with 0:")
    read_lines("my_file_0.txt")
    print("--")
    print("Full content with 4:")
    read_lines("my_file_0.txt", 4)
