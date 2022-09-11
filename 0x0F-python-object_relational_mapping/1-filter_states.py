#!/usr/bin/python3
"""
Script lists all the name in a database
starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], password=argv[2], database=argv[3]
    )

    cur = con.cursor()
    cur.execute('SELECT * FROM states WHERE name \
                 LIKE BINARY "N%" ORDER BY id ASC;')
    db = cur.fetchall()

    for i in db:
        print(i)
