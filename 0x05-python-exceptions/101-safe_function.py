#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        execute = fct(*args)
        return (execute)
    except Exception as i:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
