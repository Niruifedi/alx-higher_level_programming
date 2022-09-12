#!/usr/bin/python3
"""
script takes the name of a state aas argument
prints out the list of cities in that state
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
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = '{}';".format(argv[4],))
    db = cur.fetchall()

    for i in db:
        print(i)
