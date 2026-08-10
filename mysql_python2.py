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
    #mycursor.execute("CREATE DATABASE school")
    mycursor.execute("SHOW DATABASES")
    for c in mycursor.fetchall():
        print(c)

    q='''
    CREATE TABLE students(
    roll_no INT PRIMARY KEY,
    fullname VARCHAR(50),
    gender VARCHAR(6),
    marks INT
    )
    '''
    q1='''
    CREATE TABLE staff(
    staffid INT PRIMARY KEY,
    staffname VARCHAR(50),
    education VARCHAR(20),
    subject VARCHAR(20)
    )
    '''
    #mycursor.execute(q1)
    mycursor.execute("SHOW TABLES")
    for c in mycursor.fetchall():
        print(c)

    