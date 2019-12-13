#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    nameSearch = argv[4]

    db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = %(username)s""", {'username': username})
    rows = cursor.fetchall()
    for row in rows:
        print(row)

