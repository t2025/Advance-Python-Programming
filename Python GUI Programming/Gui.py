from tkinter import *
from tkinter import ttk
import pymysql

root=Tk()
root.geometry("800x400")
tree=ttk.Treeview(root)
db=pymysql.connect("localhost","root","root","Python_App")
cursor=db.cursor()
tree['column']=('sname','fname','address','mobile')
tree.column("sname",width=100)
tree.column("fname",width=100)
tree.column("address",width=100)
tree.column("mobile",width=100)
tree.heading("sname",text="sname")
tree.heading("fname",text="fname")
tree.heading("address",text="address")
tree.heading("mobile",text="mobile")

sql="SELECT * FROM student"
try:
    cursor.execute(sql)
    rows=cursor.fetchall()
    for row in rows:
       
        sname=row[0]
        fname=row[1]
        address=row[2]
        mobile=row[3]
        sid=row[4]
        tree.insert("",sid,text=sid,values=(sname,fname,address,mobile))
except:
    print("Database connection error")

cursor.close()
db.close()
tree.pack()
root.mainloop()