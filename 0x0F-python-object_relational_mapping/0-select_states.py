#!/usr/bin/python3

import MySQLdb
import sys

if len(sys.argv) >= 4:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM states")
    for row in rows:
        print(row)

cur.close()
conn.close()
