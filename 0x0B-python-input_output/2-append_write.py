#!/usr/bin/python3
"""
2-write_file.py
"""


def append_write(filename="", text=""):
    """ appends text in a file"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
