#!/usr/bin/python3
"""
    A script that takes an input and matches its value hbtn_0e_0_usa
    It should be safe from SQL injection
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT * FROM states
                WHERE name LIKE BINARY %s
                ORDER BY id ASC"""
    cur.execute(query,(sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
