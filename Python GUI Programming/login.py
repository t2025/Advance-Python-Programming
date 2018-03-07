from tkinter import *
import tkinter as ttk
import pymysql
root=Tk()
root.geometry("260x110")
root.title("Login form")
db=pymysql.connect("localhost","root","root","Login")
cursor=db.cursor()
def insert():
    try:
        sql="select username,password from login_details where username='%s' and password='%s'" %(e1.get(), e2.get())
        cursor.execute(sql)
        rows=cursor.fetchall()
        for row in rows:
            print("success")
    except:
        print("Database connection error")

Label(root,text="User Login form",fg="green").grid(row=0,column=1)
Label(root,text="User name").grid(row=2,column=0)
e1=Entry(root,width=30)
e1.grid(row=2,column=1)
Label(root,text="Password").grid(row=3,column=0)
e2=Entry(root,width=30,show="*")
e2.grid(row=3,column=1)
button=Button(root,text="login" ,command=insert)
button.grid(row=4,column=1)
x=(root.winfo_screenwidth()-root.winfo_reqwidth())/2
y=(root.winfo_screenheight()-root.winfo_reqheight())/2
root.geometry("+%d+%d"%(x,y))

root.mainloop()
