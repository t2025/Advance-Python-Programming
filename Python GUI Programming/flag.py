from tkinter import *
import tkinter as ttk
master=Tk()
w=Canvas(master,width=200,height=100)
w.pack()
w.create_rectangle(50,20,150,50 , fill="orange")
w.create_rectangle(50,50,150,80,fill="white")
w.create_oval(55,50,155,80)
w.create_rectangle(50,80,150,110,fill="green")
mainloop()
