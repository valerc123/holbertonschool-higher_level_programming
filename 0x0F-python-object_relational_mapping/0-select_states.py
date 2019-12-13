#!/usr/bin/python3
import sys
import MySQLdb

argv = sys.argv
username = argv[1]
passwd = argv[2]
database = argv[3]

db = MySQLdb.connect(host='localhost',
                     user=username,
                     passwd=passwd,
                     db=database)
cursor = db.cursor()
cursor.execute("SELECT * FROM states")
rows = cursor.fetchall()
for row in rows:
    print (row)
