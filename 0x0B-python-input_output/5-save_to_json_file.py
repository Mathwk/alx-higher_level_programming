#!/usr/bin/python3
"""
5-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """ Saves a json in a file"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
