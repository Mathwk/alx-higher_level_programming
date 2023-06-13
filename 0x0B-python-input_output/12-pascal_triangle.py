#!/usr/bin/python3
"""
14-pascal_triangle.py
"""


def pascal_triangle(n):
    """ Prints pascal triangle """
    if n <= 0:
        return []
    t = []
    for i in range(n):
        r = [1]
        if i > 0:
            for j in range(i):
                r.append(sum(t[-1][j:j+2]))
        t.append(r)
    return t
