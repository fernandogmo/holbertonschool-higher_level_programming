#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

if __name__ == '__main__':
    from sys import argv
    to_json_file = __import__("7-save_to_json_file").save_to_json_file
    from_json_file = __import__("8-load_from_json_file").load_from_json_file

    filename = "add_item.json"

    try:
        json_list = from_json_file(filename)
    except Exception as e:
        json_list = []
        with open(filename, 'w+') as f:
            pass

    for arg in argv[1:]:
        json_list.append(arg)

    to_json_file(json_list, filename)
