#!/usr/bin/python3
#program to print numbers from 00 to 99

for n in range(0, 99):
    print("{0:02d}".format(n), end=", ")
print("{:d}".format(99))
