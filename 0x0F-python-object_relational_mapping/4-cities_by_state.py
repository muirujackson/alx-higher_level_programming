#!/usr/bin/python3
""" a script that lists all cities from the database """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
        )
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states ON cities.state_id \
            = states.id ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    cursor.close()
    conn.close()
