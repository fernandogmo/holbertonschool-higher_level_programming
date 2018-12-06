#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    else:
        s = "arguments" if argc > 2 else "argument"
        print("{} {}:".format(argc - 1, s))
        for i, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, arg))
