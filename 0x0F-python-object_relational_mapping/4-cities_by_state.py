#!/usr/bin/python3
"""
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Save arguments in variables
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    # Create connection
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()
    cursor.execute("SELECT cities.state_id, cities.name, states.name "
                   "FROM cities JOIN states ON states.id = cities.state_id "
                   "ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
