#!/usr/bin/python3
""" lists all states from database """
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", 
                         user=username, passwd=password,
                         db=database, port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()