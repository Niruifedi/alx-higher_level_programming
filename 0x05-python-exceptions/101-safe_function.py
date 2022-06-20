#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
        return func
    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
