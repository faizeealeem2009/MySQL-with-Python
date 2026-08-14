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
    q2='''
    CREATE TABLE subject(
    subjectname VARCHAR(20),
    subjectsmarks INT(10)
    )
    '''
    #mycursor.execute(q2)
    #mycursor.execute("SHOW TABLES")
    #for x in mycursor.fetchall():
        #print(x)

    q3='''
    INSERT INTO students(roll_no,fullname,gender,marks) values(%s,%s,%s,%s)
    '''
    v=(33,"Ali","Male",467)
    v1=(43,"Yasmeen","Female",500)
    v2=(31,"Musaddique","Male",300)
    v3=(50,"Farhan","Male",550)
    v4=(56,"Izhan","Male",580)

    vlist=[
        (12,"Musaddique Seth","Male",350),
        (13,"Musaddique Bade Seth","Male",420),
        (15,"Farhan Seth","Male",550),
        (14,"Abdullah","Male",350),
        (16,"Sarim","Male",450),
        (17,"Ibrahim","Male",380),
        (18,"Saad","Male",710),
        (19,"Naif","Male",690)
    ]
    # mycursor.execute(q3,v)
    # conn.commit()
    # mycursor.execute(q3,v1)
    # conn.commit()
    # mycursor.execute(q3,v2)
    # conn.commit()
    # mycursor.execute(q3,v3)
    # conn.commit()
    # mycursor.execute(q3,v4)
    # conn.commit()
    # mycursor.executemany(q3,vlist)
    # conn.commit()
    mycursor.execute("SELECT * FROM students")
    for x in mycursor.fetchall():
        print(x)