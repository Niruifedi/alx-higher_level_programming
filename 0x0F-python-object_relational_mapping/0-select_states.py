#!/usr/bin/python3
"""
a script that lists all the states
from the database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    con = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], password=argv[2], database=argv[3]
    )
    cur = con.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC;')

    db = cur.fetchall()
    for i in db:
        print(i)
