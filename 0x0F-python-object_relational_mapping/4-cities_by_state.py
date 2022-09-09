#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    # connect to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # create cursor to execute queries using SQL
    # joins two tables to retrieve cities
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM states\
INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
