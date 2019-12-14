#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    nameSearch = argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         port=3306,
                         passwd=password,
                         db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states"
                   "WHERE name = '{:s}'"
                   "ORDER BY id ASC"
                   .format(nameSearch))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
