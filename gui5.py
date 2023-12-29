"""from tkinter import *

root=Tk()
def printName():
    print("Hello my name is Aman")

b1=Button(root,text="Print my name",command=printName)
b1.pack()

root.mainloop()
"""

from tkinter import *

root=Tk()

def printName(event):
    print("Hello my name is Aman")

b1=Button(root,text="Print my name")
b1.bind("<Button-1>",printName)
b1.pack()

root.mainloop()
    
