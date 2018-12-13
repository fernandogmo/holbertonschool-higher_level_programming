#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    safe_a = (tuple_a + (0, 0))[:2]
    safe_b = (tuple_b + (0, 0))[:2]
    return tuple(map(sum, zip(safe_a, safe_b)))
