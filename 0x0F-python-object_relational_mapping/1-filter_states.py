#!/usr/bin/python3
""" Lists states with names starting with
'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password,
                         db=database, port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT DISTINCT * FROM states WHERE
                   name LIKE 'N%' ORDER BY states.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
