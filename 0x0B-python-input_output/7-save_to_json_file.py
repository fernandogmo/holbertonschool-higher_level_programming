#!/usr/bin/python3
""" module `7-save_to_json_file` provides the `save_to_json_file` function """

import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
