#!/usr/bin/python3

import MySQLdb
import sys

if len(sys.argv) >= 2:
    username = arg[1]
    password = arg[2]
    database = arg[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM states")
    for row in rows:
        print(row)

cur.close()
conn.close()
