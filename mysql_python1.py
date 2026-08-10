import mysql.connector
try:
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="bismillah"
    )
except:
    print("Unable to connect the database")
else:
    print("Connection Established")
    mycursor=conn.cursor()
    # mycursor.execute("CREATE DATABASE employees")
    mycursor.execute("SHOW DATABASES")
    for c in mycursor.fetchall():
        print(c)