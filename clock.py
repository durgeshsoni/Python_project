#====================== make a clock=======

from tkinter import *
from tkinter.ttk import *
from time import strftime
root =Tk()
root.title("Clock by Durgesh Soni")

def time():
    string =strftime("Date=%H:%M:%S:%p\n%D\n-------------------------\nMade By Durgesh Soni")
    label.config(text=string)
    label.after(1000,time)

label =Label(root,font=('poppins',30),background="black",foreground="cyan")
label.pack(anchor="center")
time()
mainloop()