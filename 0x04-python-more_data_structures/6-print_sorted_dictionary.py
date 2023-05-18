#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_l = list(a_dictionary.keys())
    sorted_l.sort()
    for i in sorted_l:
        print("{}: {}".format(i, a_dictionary.get(i)))
