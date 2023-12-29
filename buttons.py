from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="I clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
# state, padx, pady
myButton.pack()

root.mainloop()