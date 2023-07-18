from tkinter import *
parent = Tk()
parent.geometry("200x100")

redbtn = Button(parent,text="RED",fg="red",activebackground="pink",pady=10)
bluebtn = Button(parent,text="Blue",fg="blue",activebackground="pink",pady=10)
greenbtn = Button(parent,text="Green",activeforeground="green",bg="pink",pady=10)
blackbtn = Button(parent,text="Black",activeforeground="black",bg="pink",pady=10)

redbtn.pack(side="left")
greenbtn.pack(side="right")
bluebtn.pack(side="top")
blackbtn.pack(side="bottom")

parent.mainloop()