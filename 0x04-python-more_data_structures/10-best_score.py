#!/usr/bin/python3

""" function returns a key with the biggest integer value """


def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    return max(a_dictionary)
