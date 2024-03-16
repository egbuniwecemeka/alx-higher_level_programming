#!/usr/bin/python3

import MySQLdb
import sys

if len(sys.argv) >= 2:
    username = arg[1]
    password = arg[2]
    database = arg[3]

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
        cur = conn.cursor()

        rows = cur.execute("SELECT * FROM states ORDER BY id ASC")
        for row in rows:
            print(row)

    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print("{}: {}".format(argv[0], argv[1]))
    sys.exit(1)
