#!/usr/bin/python3
"""
A function that access the database lists all states that begin with n.
No dupes
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT MIN(id) AS id, name FROM states "
                "WHERE name LIKE 'n%' GROUP BY name ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()