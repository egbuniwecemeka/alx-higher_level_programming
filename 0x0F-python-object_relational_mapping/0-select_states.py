#!/usr/bin/python3

import MySQLdb
import sys

if __name__ = "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM states")
    for row in rows:
        print(row)

cur.close()
conn.close()
