from tkinter import *

def self():
    selection="Value="+str(var.get())
    label.config(text=selection)
root=Tk()
var=DoubleVar()
scale=Scale(root,variable=var)
scale.pack(anchor=CENTER)

button=Button(root,text="Get scale value",command=self)
button.pack(anchor=CENTER)

label=Label(root)
label.pack()
root.mainloop()    