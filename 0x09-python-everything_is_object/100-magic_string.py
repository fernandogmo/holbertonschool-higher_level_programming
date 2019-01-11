#!/usr/bin/python3
def magic_string(static_list=[]):
    static_list.append( "Holberton")
    return ', '.join(static_list)

for i in range(10):
    print(magic_string())
