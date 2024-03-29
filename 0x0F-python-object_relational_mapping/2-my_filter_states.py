#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cursor = db.cursor()

    query = ("SELECT * FROM states "
             "WHERE name = '{}' "
             "ORDER BY id ASC".format(state_name))

    cursor.execute(query)

    row = cursor.fetchone()

    if row:
        print(row)

    cursor.close()
    db.close()
