#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 'a' and ord(i) <= 'z':
            i = chr(ord(i) - 32)
    print("{:s}".format(i), end="")
    print("")
