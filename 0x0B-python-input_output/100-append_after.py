#!/usr/bin/python3
"""
100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends the new string after below the search string
    """
    buffer = ''
    with open(filename, "r+") as f:
        for ln in f:
            buffer += ln
            if search_string in ln:
                buffer += new_string
    with open(filename, 'w') as fw:
        fw.write(buffer)
