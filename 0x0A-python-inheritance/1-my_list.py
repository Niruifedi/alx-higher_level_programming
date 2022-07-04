#!/usr/bin/python3
"""class inheritance"""


class MyList(list):
    """ Mylist inherits from the list superclass.
    """
    def print_sorted(self):
        """prints out a sorted list.
        """
        print(sorted(self))
