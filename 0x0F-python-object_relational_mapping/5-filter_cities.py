#!/usr/bin/python3
"""
script takes the name of a state aas argument
prints out the list of cities in that state
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    cont = 0
    con = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], password=argv[2],
        database=argv[3], charset="utf8"
    )
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = '{}';".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    #     if row[2] == argv[4]:
    #         if cont > 0:
    #             print(", ", end="")
    #         print(row[1], end="")
    #         cont = cont + 1
    # print()