#!/usr/bin/python3
"""
Script diplays content of a table
This is a more secure script against SQL injection
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], password=argv[2],
        database=argv[3]
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \
                %s ORDER BY id ASC", (argv[4],))
    db = cur.fetchall()

    for i in db:
        print(i)
