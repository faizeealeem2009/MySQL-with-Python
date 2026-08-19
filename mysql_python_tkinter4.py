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
    mycursor=conn.cursor()
    #mycursor.execute("SELECT * FROM students")
    #for c in mycursor.fetchall():
        #print(c)
    
    def display_record():
        selected_roll_no=r.get()
        mycursor.execute("SELECT * FROM students")
        for c in mycursor.fetchall():
            print(c)

        q=f'''
        SELECT * FROM students
        WHERE roll_no={selected_roll_no}
        '''
        mycursor.execute(q)
        r1=list(mycursor.fetchall())
        if len(r1)==0:
            L6.config(text="")
            L7.config(text="")
            L8.config(text="")
            L9.config(text="")
            messagebox.showerror("Error","Record Not Found!")
        else:
            L6.config(text=r1[0][0])
            L7.config(text=r1[0][1])
            L8.config(text=r1[0][2])
            L9.config(text=r1[0][3])
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
    L6=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5)
    L6.grid(row=2,column=0,padx=5,pady=5)

    L7=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5)
    L7.grid(row=2,column=1,padx=5,pady=5)

    L8=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5)
    L8.grid(row=2,column=2,padx=5,pady=5)
    
    L9=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5)
    L9.grid(row=2,column=3,padx=5,pady=5)
    root.mainloop()