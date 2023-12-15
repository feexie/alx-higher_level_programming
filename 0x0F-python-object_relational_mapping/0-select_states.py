#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user='feexie', passwd='kdkbdkku', db='hbtn_0e_0_usa')

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SELECT query to get all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        # Close the database connection
        if db:
            db.close()

