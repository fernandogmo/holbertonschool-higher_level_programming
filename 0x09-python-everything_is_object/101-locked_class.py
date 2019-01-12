#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __init__(self, name="Fernando"):
        self.first_name = name


if __name__ == '__main__':
    lc = LockedClass()
    lc.first_name = "Fernando"
    print(lc.first_name)
    try:
        lc.last_name = "Gonzalez"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
