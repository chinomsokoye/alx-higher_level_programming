#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    # connect to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # create cursor to execute queries using SQL
    # filter names starting with 'N'
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
