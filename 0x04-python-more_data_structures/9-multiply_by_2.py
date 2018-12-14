#!/usr/bin/python3
def multiply_by_2(d):
    return dict(zip(d.keys(), map(lambda x: 2*x, d.values())))
