from tkinter import *
parent = Tk()
parent.geometry("200x150")

rcheckvar = IntVar()
gcheckvar = IntVar()
bcheckvar = IntVar()

redchkbtn = Checkbutton(parent,text="Red",fg="red",variable=rcheckvar, onvalue=1, offvalue=0, height=2, width=10)
bluechkbtn = Checkbutton(parent,text="Blue",fg="blue",variable=bcheckvar, onvalue=1, offvalue=0, height=2, width=10)
greenchkbtn = Checkbutton(parent,text="Green",fg="green",variable=gcheckvar, onvalue=1, offvalue=0, height=2, width=10)

redchkbtn.pack()
greenchkbtn.pack()
bluechkbtn.pack()


parent.mainloop()