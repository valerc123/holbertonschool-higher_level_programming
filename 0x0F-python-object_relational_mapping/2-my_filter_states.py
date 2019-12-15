#!/usr/bin/python3
"""
    Displays all values in the states table where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE BINARY '{:s}' "
                   "ORDER BY id ASC".format(sys.argv[4]))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
