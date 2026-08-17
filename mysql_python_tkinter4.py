import mysql.connector
from tkinter import *
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="bismillah",
        database="school"
    )
except:
    print("Unable to connect!")
else:
    print("Connection Successful!")
    mycursor=conn.cursor()
    mycursor.execute("SELECT * FROM students")
    for c in mycursor.fetchall():
        print(c)
    
    root=Tk()
    root.title("Display Data")
    L1=Label(root,text="Enter Roll No:",font=("Arial",15,"bold"),padx=5,pady=5)
    L1.grid(row=0,column=0,padx=5,pady=5)
    E1=Entry(root)
    E1.grid(row=0,column=1,padx=5,pady=5)
    B1=Button(root,text="Display Record!",font=("Arial",12,"bold"),bg="green",padx=5,pady=5)
    B1.grid(row=0,column=2,padx=5,pady=5)
    L2=Label(root,text="Roll Number",font=("Arial",11,"bold"),padx=5,pady=5)
    L2.grid(row=1,column=0,padx=5,pady=5)
    L3=Label(root,text="Student Name",font=("Arial",11,"bold"),padx=5,pady=5)
    L3.grid(row=1,column=1,padx=5,pady=5)
    L4=Label(root,text="Gender",font=("Arial",11,"bold"),padx=5,pady=5)
    L4.grid(row=1,column=2,padx=5,pady=5)
    L5=Label(root,text="Marks",font=("Arial",11,"bold"),padx=5,pady=5)
    L5.grid(row=1,column=3,padx=5,pady=5)
    root.mainloop()