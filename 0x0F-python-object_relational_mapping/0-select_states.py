#!/usr/bin/python3

import MySQLdb
import sys

if __name__ = "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], conn=sys.argv[3])
    cur = conn.cursor()
    curQ = cur.execute("SELECT * FROM states")
    rows = curQ.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
