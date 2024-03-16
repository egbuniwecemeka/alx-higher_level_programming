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

>>> python3
>>> import MySQLdb
>>> MySQLdb.version_info
If (2, 1, 0, 'final', 0) then, successful
Install SQLAlchemy module version 1.4.x

* sudo pip3 install SQLAlchemy

... check if properly installed by using 'python3' to go into interactive mode

- python3

(-) import sqlalchemy

(-) sqlalchemy.__version___

**Note: The last basic point to use MySQLdb is to place 'import MYSQLdb' at the top of your script.**

## Connecting to a MySQL database

The next step in using MySQL in Python Scripts involves connecting to the database you wish to use. All Python DB-API 2.0 modules implement a function 'module_name.connect'. This is the function that is used to connect to the database, in our case MySQL.

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASSWORD, db=MY_DB)
eg
conn = MySQL.connect(host="localhost", port=3306, user="root", passwd="****", db=my_db", char="utf8")

This function passes the parameters to the Python extension _mysql.  This lets you pass many of the MySQL specific connection parameters through the normal connection method.

## Getting a cursor
