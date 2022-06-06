#!/usr/bin/python3

"""function returns length of tuple characters and its first character"""


def multiple_returns(sentence):
    length = len(sentence)
    f_s = sentence[0] if length > 0 else "None"
    return(length, f_s)
