#!/usr/bin/python3
"""Takes in the name of a state as an argument
Lists all cities of that state using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    # connect to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # create cursor to execute queries using SQL
    # joins two tables to retrieve cities
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
ON states.id = cities.state_id WHERE states.name = %s\
ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
