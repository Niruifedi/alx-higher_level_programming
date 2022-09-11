#!/usr/bin/python3
"""
Script that takes an argument
Displays all the values in states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], password=argv[2],
        database=argv[3]
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \
            '{:s}' ORDER BY id ASC;".format(argv[4]))
    db = cur.fetchall()

    for i in db:
        if i[1] == argv[4]:
            print(i)
