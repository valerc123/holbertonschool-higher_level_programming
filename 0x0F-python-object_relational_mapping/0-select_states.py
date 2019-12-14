#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    # Take arguments
    argv = sys.argv
    username = argv[1]
    passwd = argv[2]
    database = argv[3]
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=passwd,
                         db=database)
    # create a cursor object
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    # Take all the arguments
    rows = cursor.fetchall()
    for row in rows:
        print(row)
