from tkinter import *

root = Tk()

e = Entry(root, borderwidth=5)
e.pack()
e.insert(0,"Enter your name")

def myClick():
    myLabel = Label(root, text="Hola " + e.get())
    myLabel.pack()

myButton = Button(root, text="Click Me", command=myClick)
# state, padx, pady
myButton.pack()

root.mainloop()