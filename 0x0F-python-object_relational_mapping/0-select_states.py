#!/usr/bin/python3

import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

cur = conn.cursor()

rows = cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in rows:
    print("(%d, %s)" % (row[0], row[1]))
