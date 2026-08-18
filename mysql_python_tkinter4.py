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
    
    def display_record():
        print(r.get())
        
    root=Tk()
    root.title("Display Data")
    r=StringVar()

    L1=Label(root,text="Enter Roll No:",font=("Arial",15,"bold"),padx=5,pady=5)
    L1.grid(row=0,column=0,padx=5,pady=5)

    E1=Entry(root,textvariable=r)
    E1.grid(row=0,column=1)

    B1=Button(root,text="Display Record!",command=display_record,font=("Arial",12,"bold"),bg="green",padx=5,pady=5)
    B1.grid(row=0,column=2,padx=5,pady=5)

    L2=Label(root,text="Roll Number",font=("Arial",11,"bold"),padx=5,pady=5)
    L2.grid(row=1,column=0,padx=5,pady=5)

    L3=Label(root,text="Student Name",font=("Arial",11,"bold"),padx=5,pady=5)
    L3.grid(row=1,column=1,padx=5,pady=5)

    L4=Label(root,text="Gender",font=("Arial",11,"bold"),padx=5,pady=5)
    L4.grid(row=1,column=2,padx=5,pady=5)

    L5=Label(root,text="Marks",font=("Arial",11,"bold"),padx=5,pady=5)
    L5.grid(row=1,column=3,padx=5,pady=5)

    #Display Record
    L6=Label(root,text="1",font=("Arial",11,"bold"),padx=5,pady=5)
    L6.grid(row=2,column=0,padx=5,pady=5)

    L7=Label(root,text="Ali",font=("Arial",11,"bold"),padx=5,pady=5)
    L7.grid(row=2,column=1,padx=5,pady=5)

    L8=Label(root,text="Male",font=("Arial",11,"bold"),padx=5,pady=5)
    L8.grid(row=2,column=2,padx=5,pady=5)
    
    L9=Label(root,text="450",font=("Arial",11,"bold"),padx=5,pady=5)
    L9.grid(row=2,column=3,padx=5,pady=5)
    root.mainloop()