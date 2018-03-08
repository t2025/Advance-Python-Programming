from tkinter import *
import tkinter as ttk
import pymysql
root=Tk()
root.geometry("260x110")
root.title("Quiz Application")
db=pymysql.connect("localhost","root","root","quiz")
cursor=db.cursor()
def insert():
    try:
         sql="select username,password from admin where username='%s' and password='%s'" %(e1.get(), e2.get())
         cursor.execute(sql)
         rows=cursor.fetchall()
         for row in rows:
            print("success")
    except:
        print("Database connection error")
#Add question
def add_question():
    
login=Toplevel(root)            
Label(login,text='Admin Login Form',fg='green').grid(row=0,column=1)
Label(login,text='Username',fg='green').grid(row=1,column=0)
e1=Entry(login,width=30)
e1.grid(row=1,column=1)
Label(login,text='Password',fg='green').grid(row=2,column=0)
e2=Entry(login,width=30)
e2.grid(row=2,column=1)
button=Button(login,text="login" ,command=insert)
button.grid(row=4,column=1)
x=(login.winfo_screenwidth()-login.winfo_reqwidth())/2
y=(login.winfo_screenheight()-login.winfo_reqheight())/2
login.geometry("+%d+%d"%(x,y))

root.mainloop()

