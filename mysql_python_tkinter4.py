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
        if not selected_roll_no.strip():
            messagebox.showerror("Error", "Please Enter Roll Number!")
            return

        #mycursor.execute("SELECT * FROM students")
        #for c in mycursor.fetchall():
            #print(c)

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
    #mycursor.execute("SELECT * FROM students")
    #for c in mycursor.fetchall():
        #print(c)
        
    def delete_record():
        selected_roll_no=int(r.get())

        q1=f'''
            DELETE FROM students
            WHERE roll_no={selected_roll_no}
            '''
        try:
            mycursor.execute(q1)
            conn.commit()
            messagebox.showinfo("Deleted","Record Deleted Successfully!")
            L6.config(text="")
            L7.config(text="")
            L8.config(text="")
            L9.config(text="")
            q2=f'''
                SELECT * FROM students
                '''
            mycursor.execute(q2)
            for s in mycursor.fetchall():
                print(s)
        except:
            messagebox.showerror("Error","Record Not Found")
        
    root=Tk()
    root.title("Display Data")
    root.geometry("700x220")
    root.configure(bg="#10233f")

    label_color="#eaf2ff"
    input_bg="#f4f8ff"
    input_fg="#10233f"
    accent_color="#20c997"
    panel_color="#1b3a61"
    r=StringVar()

    L1=Label(root,text="Enter Roll No:",font=("Arial",15,"bold"),padx=5,pady=5,
             bg="#10233f",fg=label_color)
    L1.grid(row=0,column=0,padx=5,pady=5)

    E1=Entry(root,textvariable=r,bg=input_bg,fg=input_fg,
             insertbackground=input_fg,relief=FLAT)
    E1.grid(row=0,column=1)

    B1=Canvas(root,width=170,height=44,bg="#10233f",highlightthickness=0,
              cursor="hand2")
    B1.create_rectangle(20,2,150,42,fill=accent_color,outline=accent_color)
    B1.create_rectangle(2,20,168,24,fill=accent_color,outline=accent_color)
    B1.create_oval(2,2,42,42,fill=accent_color,outline=accent_color)
    B1.create_oval(128,2,168,42,fill=accent_color,outline=accent_color)
    B1.create_text(85,22,text="Display Record!",fill="#06291f",
                   font=("Arial",12,"bold"))
    B1.bind("<Button-1>",lambda event: display_record())
    B1.grid(row=0,column=2,padx=5,pady=5)

    L2=Label(root,text="Roll Number",font=("Arial",11,"bold"),padx=5,pady=5,
             bg=panel_color,fg=label_color)
    L2.grid(row=1,column=0,padx=5,pady=5)

    L3=Label(root,text="Student Name",font=("Arial",11,"bold"),padx=5,pady=5,
             bg=panel_color,fg=label_color)
    L3.grid(row=1,column=1,padx=5,pady=5)

    L4=Label(root,text="Gender",font=("Arial",11,"bold"),padx=5,pady=5,
             bg=panel_color,fg=label_color)
    L4.grid(row=1,column=2,padx=5,pady=5)

    L5=Label(root,text="Marks",font=("Arial",11,"bold"),padx=5,pady=5,
             bg=panel_color,fg=label_color)
    L5.grid(row=1,column=3,padx=5,pady=5)

    #Display Record
    L6=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5,
             bg="#244b78",fg=accent_color)
    L6.grid(row=2,column=0,padx=5,pady=5)

    L7=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5,
             bg="#244b78",fg=accent_color)
    L7.grid(row=2,column=1,padx=5,pady=5)

    L8=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5,
             bg="#244b78",fg=accent_color)
    L8.grid(row=2,column=2,padx=5,pady=5)
    
    L9=Label(root,text="",font=("Arial",11,"bold"),padx=5,pady=5,
             bg="#244b78",fg=accent_color)
    L9.grid(row=2,column=3,padx=5,pady=5)
    
    B2=Button(root,text="Delete Record",fg="white",command=delete_record,font=("Arial",12,"bold"),bg="red",padx=5,pady=5)
    B2.grid(row=3,column=0,padx=5,pady=5)
    root.mainloop()