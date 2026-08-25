import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="bismillah",
        database="school"
    )
except:
    print("Unable to connect the database")
else:
    print("Connection Established")
    mycursor=conn.cursor()
    mycursor.execute("SELECT * FROM students")
    for c in mycursor.fetchall():
        print(c)
    