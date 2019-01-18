#!/usr/bin/python3
""" module `8-load_to_json_file` provides the `load_to_json_file` function """

import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
