from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x200")

w = Label(root, text ='Messagebox Demo', font = "50")
w.pack()
# Hide the main window
# root.withdraw()

# Show a message box
messagebox.showinfo("info", "This is a message box!")
messagebox.showwarning("warning", "warning!")
messagebox.showerror("error", "error!")

messagebox.askquestion("askquestion", "sure ?")
messagebox.askyesno("askyesno", "confirm ?")
messagebox.askokcancel("askokcancel", "continue ?")
messagebox.askyesnocancel("askyesnocancel", "continue ?")
messagebox.askretrycancel("askretrycancel", "try again !")

# Close the Tkinter window
# root.destroy()
root.mainloop()