from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("homework alert", "mom: if you do not do homework i will hack your computer")
    messagebox.askyesno("homework alert", "mom: are you doing homework?")
    messagebox.showinfo("homework alert", "mom: fine i will help: 8x9 = 72")
    messagebox.askyesno("homework alert", "mom: do you want to go to school?")
    messagebox.showwarning("homework alert", "mom: else i will kill you")
button = Button(root, text = "skip homework", command = msg)
button.place(x=40, y=80)
root.mainloop()