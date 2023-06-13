#!/usr/bin/python3
"""
2-read_lines.py
"""


def read_lines(filename="", nb_lines=0):
    """ read the lines of a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        if nb_lines <= 0:
            for line in file:
                print(line, end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
