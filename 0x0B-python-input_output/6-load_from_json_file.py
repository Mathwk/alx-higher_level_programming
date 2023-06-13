#!/usr/bin/python3
"""
6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """loads a json from a file"""
    with open(filename, encoding='utf8') as f:
        return json.loads(f.read())
