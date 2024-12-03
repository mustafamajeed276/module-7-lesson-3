from tkinter import *
window = Tk()
window.title("event handler")
window.geometry('100x100')
def handle_keypress(event):
    print(event.char)
window.bind('<Key>', handle_keypress)
def handle_click(event):
    name = input("hello, who pressed the button?")
    print("well, ", name, " thanks for waking me up!!")
button = Button(text = "click!!")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()