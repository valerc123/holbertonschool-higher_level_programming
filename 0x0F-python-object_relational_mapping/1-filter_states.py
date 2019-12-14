#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    # Take arguments
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    # Connect to a MySQL server
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()
    # Run query
    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE BINARY 'N%' "
                   "ORDER BY states.id ASC")
    # Fetch all fields
    rows = cursor.fetchall()
    # Print fields
    for row in rows:
            print(row)
