#!/usr/bin/python3
"""
    List all cities from the database hbtn_0e_4_usa
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
                   "FROM cities JOIN states "
                   "ON cities.state_id = states.id "
                   "ORDER BY cities.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
