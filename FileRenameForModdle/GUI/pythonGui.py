import tkinter as tk
from tkinter import *
from rename import calculate
import os


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    print("You selected the option " + str(var.get()))
    global changed,unchanged,path
    path = e1.get()
    try:
        changed, unchanged = calculate(e1.get(),e2.get(),e3.get(),var.get())
    except:
        LbChange.insert(END,"Error")
        return
    LbChange.delete(0,END)
    for files in unchanged:
        LbUnchanged.insert(END,files)
    for files in changed:
        LbChange.insert(END,files[0]+" ------> "+ files[1])
    tk.Button(master, 
          text='Cancel', 
          command=sclear).grid(row=9, 
                                    column=2, 
                                    sticky=tk.W, 
                                    pady=4)
    tk.Button(master, 
              text='Change', command=rename).grid(row=9, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                           pady=4)

def sclear():
    LbChange.delete(0,END)
    LbUnchanged.delete(0,END)
def clearall():
    sclear()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')

def rename():
    print("here")
    for names in changed:
        print("haai"+names[0])
        os.rename(os.path.join(path,names[0]),os.path.join(path,names[1]))
    sclear()

def sel():
   print("You selected the option " + str(var.get()))
   
master = tk.Tk()
master.title("Rename File")
master.geometry("550x600")
tk.Label(master, 
         text="Path",anchor='w').grid(row=0,sticky='w')
tk.Label(master, 
         text="Common Prefix").grid(row=1,sticky='w')
tk.Label(master, 
         text="Number of total character to be extracted\n(Usually 7 for roll)").grid(row=2,sticky='w')

e1 = tk.Entry(master,width=40)
e2 = tk.Entry(master,width=40)
e3 = tk.Entry(master,width=40)

e1.grid(row=0, column=1, columnspan=2)
e2.grid(row=1, column=1, columnspan=2)
e3.grid(row=2, column=1 , columnspan=2)


var = IntVar()
var.set(1)
R1 = Radiobutton(master, text="A55A ---> 55_AA", variable=var, value=1,
                  command=sel)
R1.grid( row = 3,sticky='w' )

R2 = Radiobutton(master, text="A55A ---> 55_A55A", variable=var, value=2,
                  command=sel)
R2.grid( row = 4,sticky='w' )


tk.Label(master, 
         text="Changed",anchor='w').grid(row=6,sticky='w')
tk.Label(master, 
         text="Unchanged").grid(row=6, column = 1,sticky='w')
scrollbar = Scrollbar(master)
scrollbar.grid(row = 8,sticky="ew")

LbChange = Listbox(master,width=50,height=20)
LbChange.grid(row=7)
LbUnchanged = Listbox(master,width=40,height=20)
LbUnchanged.grid(row=7,column = 1,columnspan=2)
scrollbar.config(orient='horizontal',command = LbChange.xview)
#LbChange.config(xscrollcommand = scrollbar.set)

tk.Button(master, 
          text='Cancel', 
          command=clearall).grid(row=5, 
                                    column=2, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Ok', command=show_entry_fields).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)



tk.mainloop()

