#!/usr/bin/python3.8

if __name__ == '__main__':
    import hidden_4

    name = dir(hidden_4)

    for n in name:
        if n[:2] != '__':
            print("{:s}".format(n))
