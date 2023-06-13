#!/usr/bin/python3
"""
number_of_lines
"""


def number_of_lines(filename=""):
    """Prints the number of lines in the file"""
    with open(filename, encoding='utf8') as f:
        lines = 0
        for ln in f:
            lines += 1
        return lines
