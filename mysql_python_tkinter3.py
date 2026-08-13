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

    root=Tk()
    root.title("Student Regestration Form")
    root.geometry("400x300")

    l1=Label(root,text="Enter Roll No:")
    l1.grid(row=0,column=0,padx=5,pady=5)
    e1=Entry(root,textvariable=rollNumber)
    e1.grid(row=0,column=1)

    l2=Label(root,text="Enter Full Name:")
    l2.grid(row=1,column=0,padx=5,pady=5)
    e2=Entry(root,textvariable=Fullname)
    e2.grid(row=1,column=1)

    l3=Label(root,text="Select Gender:")
    l3.grid(row=2,column=0,padx=5,pady=5)
    
    root.mainloop()