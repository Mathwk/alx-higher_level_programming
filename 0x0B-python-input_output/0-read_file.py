#!/usr/bin/python3
"""
0-read_file.py
"""


def read_file(filename=""):
    """ Prints a file """
    with open(filename, encoding='utf8') as f:
        for ln in f:
            print(ln, end='')
