from tkinter import *
import tkinter as ttk
root=Tk()
root.title("Practise")
#Button in tkinter 
b=ttk.Button(text="Hello Tkinter")
b.pack()

#Canvas in Tkinter 
c=ttk.Canvas(bg='blue',height=200,width=100)
c.pack()
#Checkbutton in Tkinter 
checkvar1=IntVar()
checkvar2=IntVar()
c1=ttk.Checkbutton(root,text="Cricket",variable=checkvar1,onvalue=1,offvalue=0,height=5,width=20)
c2=ttk.Checkbutton(root,text="Football",variable=checkvar2,onvalue=1,offvalue=0,height=5,width=20)
c1.pack()
c2.pack()
#Label and Entry in Tkinter 
l=ttk.Label(root,text="My label")
l.pack()
e=ttk.Entry(root,bd=5)
e.pack()
#Listbox examples
lb=ttk.Listbox(root)
lb.insert(1,"Python")
lb.insert(2,"Java")
lb.insert(3,"C#")
lb.insert(4,"Scala")
lb.pack()
#Menu Button
mb=ttk.Menubutton(root,text="MenuButton",relief=RAISED)
mb.grid()
mb.menu()=Menu(mb,tearoff=0)
mb['menu']=mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

mb.pack()


root.mainloop()








