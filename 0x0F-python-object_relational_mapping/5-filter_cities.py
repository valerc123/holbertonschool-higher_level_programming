#!/usr/bin/python3
"""
    Script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    # Save arguments in variables
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    # Create connection
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name "
                   "FROM cities JOIN states "
                   "ON cities.state_id = states.id "
                   "WHERE states.name LIKE BINARY %(state)s"
                   "ORDER BY cities.id ASC", {'state': state})
    rows = cursor.fetchall()
    print(", ".join(map(lambda row: row[0], rows)))
