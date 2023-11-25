#!/usr/bin/python3
"""
A function that access the database lists all states that begin
with command line argv 4.
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    state_name = argv[4]
    cur = conn.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '{}%' "
                "ORDER BY states.id ASC".format(state_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
