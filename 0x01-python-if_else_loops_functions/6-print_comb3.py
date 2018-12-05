#!/usr/bin/python3
for first in range(0, 10):
        for i in range(first+1, 10):
                if first < 8:
                        print('{}{}'.format(first, i), end=', ')
                else:
                        print('{}{}'.format(first, i))
