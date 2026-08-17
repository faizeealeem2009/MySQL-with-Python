import mysql.connector
from tkinter import *
from tkinter import messagebox
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
    def submit_data():
        print("Data Submitted!")
        print(rollNumber.get())
        print(Fullname.get())
        print(gender.get())
        print(marks.get())

        mycursor=conn.cursor()
        q='''
        INSERT INTO students(roll_no,fullname,gender,marks) values(%s,%s,%s,%s)
        '''
        v=(rollNumber.get(),Fullname.get(),gender.get(),marks.get())
        mycursor.execute(q,v)
        conn.commit()

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)

        messagebox.showinfo("Record Added!","Record Added Successfully!")
        conn.close()

    root=Tk()
    root.title("Student Regestration Form")
    root.geometry("400x300")

    rollNumber=StringVar()
    Fullname=StringVar()
    gender=StringVar()
    marks=StringVar()


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

    r1=Radiobutton(root,text="Male",variable=gender,value="Male")
    r1.grid(row=3,column=0)
    r2=Radiobutton(root,text="Female",variable=gender,value="Female")
    r2.grid(row=3,column=1)

    l4=Label(root,text="Enter Marks:")
    l4.grid(row=4,column=0,padx=5,pady=5)
    e3=Entry(root,textvariable=marks)
    e3.grid(row=4,column=1)

    B1=Button(root,text="Add Record!",command=submit_data,padx=10,pady=10)
    B1.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
    root.mainloop()
