# 0x0F. Python - Object-relational mapping

## Object -relational Mappers(ORMS)

code library used to automate the automtic transfer of relational databases to object more commonly used in application codes. ORMs represent a bridge between the tables, relationships and fields of relational databases and Python objects.

Usefulness of ORMs
Allows developers to use Python to create, read, update and delete, instead of MYSQL in basesdata. This means programmers can use the language they are comfortable instead of writing SQL schemas and procedures.

Downsides of ORM
complexities in databases can be transferred to application code
Reduced performance
Impedance mismatch.

Introduction to MySQL python

MySQL Python is the MySQL driver for the python language. It is made up of the _mysql wrapper and DB-API 2.0 module MySQLdb. As devs importing MySQL into Python Scripts the DB-API 2.0 is what we are concerned with. The MySQLdb conforms to standards set by Python PEP 249. The first step to use MySQLdb is to install it.

* Steps
Install and activate venv

Firstly, i created the python virtual environment and installed venv:

* sudo apt-get install python3.8-venv

* python3 -m venv venv

* source venv/bin/activate

Install MySQLdb module version 2.0.x

* sudo apt-get install python3-dev

* sudo apt-get install libmysqlclient-dev

* sudo apt-get install zlib1g-dev

* sudo pip3 install mysqlclient
... check if properly installed by using 'python3' to go into interactive mode

(-) python3
(-) import MySQLdb
(-) MySQLdb.version_info
If (2, 1, 0, 'final', 0) then, successful
Install SQLAlchemy module version 1.4.x

* sudo pip3 install SQLAlchemy

... check if properly installed by using 'python3' to go into interactive mode

(-) python3

(-) import sqlalchemy

(-) sqlalchemy.__version___

**Note: The last basic point to use MySQLdb is to place 'import MYSQLdb' at the top of your script.**

## Connecting to a MySQL database

The next step in using MySQL in Python Scripts involves connecting to the database you wish to use. All Python DB-API 2.0 modules implement a function 'module_name.connect'. This is the function that is used to connect to the database, in our case MySQL.

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASSWORD, db=MY_DB)
eg
conn = MySQL.connect(host="localhost", port=3306, user="root", passwd="****", db=my_db", char="utf8")

This function passes the parameters to the Python extension _mysql.  This lets you pass many of the MySQL specific connection parameters through the normal connection method.

## Getting a Cursor in MySQL Python

To make good use of this connection we have to create a cursor object. This object gives us the ability to have multiple working environment with the same connection to the database. A cursor can be created by executing the cursor function'cursor()'' on your database.

## Executin MySQL Queries in Python

Executing queries in Python involves calling the execute function on the cursor object. The 'execute' function requires one parameter, which is the query.

Note: If the query contains any substitution, then a second parameter, a tuple containing the values to substitute must be given

Example 1: Create Table:
cur.execute("(CREATE TABLE song (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL))")

Example 2: Execute Insert / Single Substitution Query
songs = (""abc, "def", "ghi")
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (%s)", song)
    print "Auto Increment ID: %s" % cur.lastrowid

Example 3: Multiple Substitution Query

cur.execute("SELECT * FROM song WHERE id=%s or id=%s", (1,2))
Note: **It is important to note that when there are multiple parameters, a tuple must be used to enclose the parameters. The parameters are then substituted using indexing.

Example 4: Execute Select

numrow = cur.execute("SELECT * FROM song")
print "Selected %s rows" % numrows  //save return value from execute stateement
print "Selected %s rows" % cur.rowcount //Python DB-API 2.0 way. It makes it easier if you hve to change databases.

## Obtaining query results

Whenever a SELECT statement is used, one of the two methods will need to be used to obtain results

* Fetch All-at-Once

Print results in comma delimited format
cur.execute("SELECT * FROM song")
cur.fetchall()      //Used to obtain multiple query results
for row in rows:
    for col in cols:
        print "%s," % col
    print '\n'

* Fetch One-at-a-Time
cur.execute("SELECT * FROM song WHERE id=1)
print "Id:%s -- Title:%s" % cur.fetchone()     //fetchone for obtaining single qury result


## Exceptions & Errors

in Python DB-API errors are indicated by raising exceptions. 'module.Error'is a top-level package used to catch all DBs exceptions. In MySQL, it is MySQLdb.Error. Every DB-API statement has the potential to raise an exception, thats why it is necessary to surround databases query with try/exception block. This includes connections, cursor requests and statement executions

Get data from database
try:
    cur.execute("SELECT * FROM song")
    row = cur.fetchall()
except MySQLdb.Error, e:
    try:
        print "MySQL Error [%d]: [%s]" % (e.argv[0], e.argv[1])
    except IndexError:
        print "MySQL Error: %s" % str(e)
Print result in comma delimited format.
for row in rows:
    for col in cols:
        print "%s" % col
    print "\n"

## Clean Up

This is easy. Firstly, close all open cursors & databases connection. Call the close function for each instance created
cur.close() //close cursors
db.close()  //close databases

