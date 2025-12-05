#!/usr/bin/python3
<<<<<<< HEAD
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()

=======
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
>>>>>>> bb10a683382ae6e7a014ed15d4c484ae05e54bc7
