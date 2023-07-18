from tkinter import *
parent = Tk()
parent.geometry("400x200")

name = Label(parent,text="name",fg="blue").place(x=30,y=30)
input_name = Entry(parent).place(x=110,y=30)
email = Label(parent,text="email",fg="blue").place(x=30,y=70)
input_email = Entry(parent).place(x=110,y=70)
submit = Button(parent,text="SUBMIT",fg="red").place(x=30,y=110)

parent.mainloop()