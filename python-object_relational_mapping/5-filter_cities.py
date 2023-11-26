#!/usr/bin/python3
"""
List all cities based on a state (argv 4). Safe from sql injection
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    state_name = argv[4]

    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON states.id = cities.state_id "
             "WHERE states.name LIKE BINARY %s "
             "ORDER BY cities.id ASC;")

    cur = conn.cursor()
    cur.execute(query, ("{}".format(state_name),))
    query_rows = cur.fetchall()

    result = ""
    for row in query_rows:
        result += row[0]
        if row != query_rows[-1]:
            result += ", "

    print(result)

    cur.close()
    conn.close()
