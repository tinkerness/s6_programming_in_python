from tkinter import *
parent = Tk()
parent.geometry("200x100")

redbtn = Button(parent,text="RED",fg="red")
bluebtn = Button(parent,text="Blue",fg="blue")
greenbtn = Button(parent,text="Green",fg="green")
blackbtn = Button(parent,text="Black",fg="black")

bluebtn.pack(side="top")
redbtn.pack(side="left")
greenbtn.pack(side="right")
blackbtn.pack(side="bottom")

parent.mainloop()