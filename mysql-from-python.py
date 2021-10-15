import os
import pymysql

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()
