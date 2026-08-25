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
        try:
            mycursor.execute(q,v)
            conn.commit()
        except mysql.connector.Error as error:
            conn.rollback()
            if error.errno == 1062:
                messagebox.showwarning("Duplicate Roll Number",
                                        "This roll number already exists. Please use a different roll number.")
            else:
                messagebox.showerror("Database Error",str(error))
            mycursor.close()
            return
        mycursor.close()

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)

        messagebox.showinfo("Record Added!","Record Added Successfully!")

    root=Tk()
    root.title("Student Regestration Form")
    root.geometry("400x300")
    root.configure(bg="#10233f")

    label_color="#eaf2ff"
    input_bg="#f4f8ff"
    input_fg="#10233f"
    accent_color="#20c997"

    def draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius, color):
        canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2,
                                fill=color,outline=color)
        canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius,
                                fill=color,outline=color)
        canvas.create_oval(x1, y1, x1 + radius * 2, y1 + radius * 2,
                           fill=color,outline=color)
        canvas.create_oval(x2 - radius * 2, y1, x2, y1 + radius * 2,
                           fill=color,outline=color)
        canvas.create_oval(x1, y2 - radius * 2, x1 + radius * 2, y2,
                           fill=color,outline=color)
        canvas.create_oval(x2 - radius * 2, y2 - radius * 2, x2, y2,
                           fill=color,outline=color)

    def rounded_box(parent, variable):
        box=Canvas(parent,width=205,height=38,bg="#10233f",highlightthickness=0)
        draw_rounded_rectangle(box,2,2,203,36,14,input_bg)
        entry=Entry(box,textvariable=variable,bg=input_bg,fg=input_fg,
                    insertbackground=input_fg,relief=FLAT,bd=0)
        box.create_window(103,19,window=entry,width=185,height=28)
        return box,entry

    rollNumber=StringVar()
    Fullname=StringVar()
    gender=StringVar()
    marks=StringVar()


    l1=Label(root,text="Enter Roll No:",bg="#10233f",fg=label_color)
    l1.grid(row=0,column=0,padx=5,pady=5)
    e1_box,e1=rounded_box(root,rollNumber)
    e1_box.grid(row=0,column=1)

    l2=Label(root,text="Enter Full Name:",bg="#10233f",fg=label_color)
    l2.grid(row=1,column=0,padx=5,pady=5)
    e2_box,e2=rounded_box(root,Fullname)
    e2_box.grid(row=1,column=1)

    l3=Label(root,text="Select Gender:",bg="#10233f",fg=label_color)
    l3.grid(row=2,column=0,padx=5,pady=5)

    r1=Radiobutton(root,text="Male",variable=gender,value="Male",
                   bg="#10233f",fg=label_color,activebackground="#10233f",
                   activeforeground=accent_color,selectcolor="#1b3a61")
    r1.grid(row=3,column=0)
    r2=Radiobutton(root,text="Female",variable=gender,value="Female",
                   bg="#10233f",fg=label_color,activebackground="#10233f",
                   activeforeground=accent_color,selectcolor="#1b3a61")
    r2.grid(row=3,column=1)

    l4=Label(root,text="Enter Marks:",bg="#10233f",fg=label_color)
    l4.grid(row=4,column=0,padx=5,pady=5)
    e3_box,e3=rounded_box(root,marks)
    e3_box.grid(row=4,column=1)

    B1=Canvas(root,width=150,height=43,bg="#10233f",highlightthickness=0,
              cursor="hand2")
    draw_rounded_rectangle(B1,2,2,148,41,18,accent_color)
    B1.create_text(75,21,text="Add Record!",fill="#06291f",
                   font=("Arial",10,"bold"))
    B1.bind("<Button-1>",lambda event: submit_data())
    B1.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
    root.mainloop()
