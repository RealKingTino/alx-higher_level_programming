#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""
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

    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))

    # Fetch all city names and join them with a comma and space
    cities = [row[0] for row in cursor.fetchall()]
    result = ", ".join(cities)

    print(result)

    cursor.close()
    db.close()
