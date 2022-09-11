#!/usr/bin/python3
"""Script to list states in a database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host='Localhost', port=3306,
        user=argv[1], password=argv[2], database=argv[3]
    )
    cur = con.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    db = cur.fetchall()
    for i in db:
        print(i)
    cur.close()