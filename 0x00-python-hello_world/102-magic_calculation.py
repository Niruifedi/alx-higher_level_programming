#!/usr/bin/python3
def magic_calculation(a, b):
    return(len(98 + a ** b))
import dis
dis.dis(magic_calculation)
