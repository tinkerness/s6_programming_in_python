from tkinter import *
parent = Tk()
parent.geometry("200x100")

name = Label(parent,text="name",fg="blue").grid(row=0,column=0)
input_name = Entry(parent).grid(row=0,column=1)
email = Label(parent,text="email",fg="blue").grid(row=1,column=0)
input_email = Entry(parent).grid(row=1,column=1)
submit = Button(parent,text="SUBMIT",fg="red").grid(row=2,column=0)

parent.mainloop()