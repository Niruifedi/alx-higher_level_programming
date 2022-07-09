#!/usr/bin/python3
import sys


def print_status():
    """print status from stdin"""
    size = 0
    counter = 0
    status_code = {'200': 0, '301': 0, '400': 0, '405': 0,
                    '401': 0, '403': 0, '404': 0, '500': 0}

    for i in sys.stdin:
        line = i.split()

        try:
            size += int(line[-1])
            code = line[-2]
            status_code[code] += 1
        except:
            continue

        if counter == 9:
            print("File size: {}".format(size))
            for key, val in status_code.items():
                if val != 0:
                    print("{}: {}".format(key, val))
            counter = 0
        counter += 1
    if counter < 9:
         print("File size: {}".format(size))
         for key, val in status_code.items():
                if val != 0:
                    print("{}: {}".format(key, val))

if __name__ == '__main__':
    print_status()
