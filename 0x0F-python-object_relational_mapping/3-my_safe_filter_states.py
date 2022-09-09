#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table
from the database hbtn_0e_0_usa
where name matches the argument, safe from MySQL injection
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    # connect to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # create cursor to execute queries using SQL
    # match argument given, safe from MySQL injection
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
