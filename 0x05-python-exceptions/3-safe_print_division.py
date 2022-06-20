#!/usr/bin/python3

"""function divides 2 integers and handles exception"""


def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print('Inside result {}'.format(result))
    return result
