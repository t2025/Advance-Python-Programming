from tkinter import *
import tkinter as ttk
#from ttk import *
root=Tk()
root.title("Combobox example")
mainframe=Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))
mainframe.pack(pady = 100, padx = 100)

tkvar=StringVar(root)
choices={'Physics','Chemistry','Biology','Maths','Computers'}
tkvar.set('Physics')
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe,text="Choose a subject").grid(row=1,column=1)
popupMenu.grid(row=2,column=1)

#change value 
def change_dropdown(*args):
    print(tkvar.get())
tkvar.trace('w',change_dropdown)
root.mainloop()

