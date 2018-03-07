from tkinter import *
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for line in range(0,100):
    mylist.insert(END,"C-DAC"+str(line))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()    