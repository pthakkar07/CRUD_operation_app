from tkinter import *
import tkinter as tk
import psycopg2  

root= Tk()

def search(id):
    conn=psycopg2.connect(dbname="postgres", user="postgres",password="", host="localhost", port="5432" )
    cur=conn.cursor()
    query='''select * from student where id=%s'''
    cur.execute(query,(id))
    row= cur.fetchone()
    print(row)
    display_search(row) 
    conn.commit()
    conn.close()

def display_all():
    conn=psycopg2.connect(dbname="postgres", user="postgres",password="", host="localhost", port="5432" )
    cur=conn.cursor()
    query='''select * from student'''
    cur.execute(query)
    row= cur.fetchall()
    print(row)
    listbox= Listbox(frame, width=20, height=5)
    listbox.grid(row=10, column=1)
    for x in row:
        listbox.insert(END,x)
    conn.commit()
    conn.close()

def display_search(row):
    listbox= Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(0,row)

def delete_item(id):
    conn=psycopg2.connect(dbname="postgres", user="postgres",password="", host="localhost", port="5432" )
    cur=conn.cursor()
    query='''delete from student where id=%s;'''

    cur.execute(query,(id))
    print("Deleted data from table")
    
    conn.commit()
    conn.close()

    delete_id.delete(0,END)
    display_all()





def get_data(name,age,address):
    conn=psycopg2.connect(dbname="postgres", user="postgres",password="", host="localhost", port="5432" )
    cur=conn.cursor()
    query='''insert into student(name,age,address) values(%s,%s,%s);'''

    cur.execute(query,(name,age,address))
    print("value added successfully into table")
    
    conn.commit()
    conn.close()
    display_all()
canvas= Canvas(root, height=480,width=900)
canvas.pack()
frame= Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8, relheight=0.8)

label= Label(frame, text="Add Data")
label.grid(row=0,column=1)

label1= Label(frame, text="Name")
label1.grid(row=1,column=0)

entry = Entry(frame)
entry.grid(row=1,column=1)

label2= Label(frame, text="Age")
label2.grid(row=2,column=0)

entry_age = Entry(frame)
entry_age.grid(row=2,column=1)


label3= Label(frame, text="Address")
label3.grid(row=3,column=0)

entry_add = Entry(frame)
entry_add.grid(row=3,column=1)

button=Button(frame, text="Add",command=lambda:get_data(entry.get(),entry_age.get(),entry_add.get()))
button.grid(row=4,column=1)

label4= Label(frame, text="Search Data")
label4.grid(row=5,column=1)

label4= Label(frame, text="Search By ID")
label4.grid(row=6,column=0)

entry_id = Entry(frame)
entry_id.grid(row=6,column=1)

button=Button(frame, text="Search",command=lambda:search(entry_id.get()))
button.grid(row=6,column=2)

label4= Label(frame, text="Delete Data")
label4.grid(row=11,column=1)

label4= Label(frame, text="delete By ID")
label4.grid(row=12,column=0)

delete_id = Entry(frame)
delete_id.grid(row=12,column=1)
button=Button(frame, text="Delete",command=lambda:delete_item(delete_id.get()))
button.grid(row=12,column=2)



display_all()

root.mainloop()