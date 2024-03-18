#!/usr/bin/python3
"""  takes an argument and lists all cities of that state, using the db  """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1]
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT cities.name FROM cities
               INNER JOIN states ON states.id=cities.state_id
               WHERE states.name=%s
               ORDER BY id ASC"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=', ')
    cur.close()
    db.close()
