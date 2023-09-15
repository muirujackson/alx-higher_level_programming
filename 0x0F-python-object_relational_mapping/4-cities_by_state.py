#!/usr/bin/env python3
""" a script that lists all cities from the database """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ connect to database """
    

    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT C.id, C.name, S.name FROM cities AS C,\
            states AS S WHERE C.state_id = S.id ORDER BY C.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    conn.close()
