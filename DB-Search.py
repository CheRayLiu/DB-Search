#!/usr/bin/python3

import tkinter as tk
import pymysql
from tkinter import ttk
from tkinter import *
def db(colnames,e1,e2,e3,e4,e5,c1,c2):
    # Open database connection
    db = pymysql.connect(host=str(e1),user =str(e2), passwd=str(e3) ,db =str(e4))

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    if (colnames != ""):
        print("SELECT " + colnames + " from " + str(e5) + "WHERE name LIKE '"+ c1+"%' AND ssn LIKE '"+ c2+ "%';")
        cursor.execute("SELECT " + colnames + " from " + str(e5) + " WHERE name LIKE '"+ c1+"%' AND ssn LIKE '"+ c2+ "%';" )

        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        string =""
        for item in data:
            for column in item:
                string += str(column)
                string += " "
            string+= "\n"
        popupdb(data)
        
    # disconnect from server
    else:
        popupmsg("","Please select at least one checkbox")
    db.close()
def popupdb(result):
    root = tk.Tk()
    tree = ttk.Treeview(root)
    tree["columns"] = ("one", "two")
    tree.column("one", width=100)
    tree.column("two", width=100)

 
    tree.heading("one", text="NAME")
    tree.heading("two", text="VOTES")
    for item in result:
       tree.insert('', 'end', values=(item[0], item[1]))
    tree.pack()
    root.mainloop()

    
def popupmsg(msg, result):
    popup = tk.Tk()
    def leavemini():
        popup.destroy()
    popup.wm_title("Result")
    if result !="":
        s = tk.Scrollbar(popup)
        T = tk.Text(popup)

        T.focus_set()
        s.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        s.config(command=T.yview)
        T.config(yscrollcommand=s.set)
        T.insert(tk.END, result)
        B1 = ttk.Button(popup, text="Okay", command=leavemini)
        B1.pack()
    else:
        label = ttk.Label(popup, text = msg, font = NORM_FONT)
        label.pack(side = "top", fill = "x", pady = 10)
        B1 = ttk.Button(popup, text = "Okay", command = leavemini)
        B1.pack()
    popup.mainloop()

def var_states(e1,e2,e3,e4,e5,c1,c2):
   col = ""
   if (var1.get() != 0):
    col += "name,"
   if (var2.get() != 0):
    col += "ssn,"



   if (col.endswith(",")):
       col = col[:-1]
   db(col,e1,e2,e3,e4,e5,c1,c2)
master = tk.Tk()
master.title("DB-Search")
tk.Label(master, text="Host").grid(row=0)
tk.Label(master, text="User").grid(row=1)
tk.Label(master, text="Password").grid(row=2)
tk.Label(master, text="Database Name").grid(row=3)
tk.Label(master, text="Table Name").grid(row=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)



tk.Label(master, text="Select/Search columns:").grid(row=5, sticky=tk.W)
var1 = tk.IntVar()
tk.Checkbutton(master, text="name", variable=var1).grid(row=6, sticky=tk.W)
var2 = tk.IntVar()
tk.Checkbutton(master, text="ssn", variable=var2).grid(row=7, sticky=tk.W)
c1 = tk.Entry(master)
c2 = tk.Entry(master)
c1.grid(row=6, column=1)
c2.grid(row=7, column=1)




tk.Button(master, text='Quit', command=master.destroy).grid(row=8, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command= lambda: var_states(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),c1.get(),c2.get())).grid(row=9, sticky=tk.W, pady=4)
tk.mainloop()
