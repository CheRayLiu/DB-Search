#!/usr/bin/python3

import tkinter as tk
import pymysql
from tkinter import ttk
def db(colnames):
    # Open database connection
    db = pymysql.connect(host="localhost",user ='root',db ="test_db" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    if (colnames != ""):
       
        cursor.execute("SELECT " + colnames + " from tab")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        string =""
        for item in data:
            for column in item:
                string += str(column)
                string += " "
            string+= "\n"
        popupmsg("",string)
        
    # disconnect from server
    else:
        popupmsg("","Please select at least one checkbox")
    db.close()

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

def var_states():
   col = ""
   print(var1.get())
   if (var1.get() != 0):
    col += "name,"
   if (var2.get() != 0):
    col += "ssn,"



   if (col.endswith(",")):
       col = col[:-1]
   db(col)
master = tk.Tk()



tk.Label(master, text="Select columns:").grid(row=0, sticky=tk.W)
var1 = tk.IntVar()
tk.Checkbutton(master, text="name", variable=var1).grid(row=1, sticky=tk.W)
var2 = tk.IntVar()
tk.Checkbutton(master, text="ssn", variable=var2).grid(row=2, sticky=tk.W)


tk.Button(master, text='Quit', command=master.destroy).grid(row=3, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command= var_states).grid(row=4, sticky=tk.W, pady=4)
tk.mainloop()
