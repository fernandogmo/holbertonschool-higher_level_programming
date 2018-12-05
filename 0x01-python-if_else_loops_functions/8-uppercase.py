#!/usr/bin/python3
def uppercase(s):
    for c in s:
        delta = ord('A') - ord('a') if ord('a') <= ord(c) <= ord('z')\
                                    else 0
        print(chr(ord(c) + delta), end="")
    print()
