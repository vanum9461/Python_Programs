from tkinter import *

root=Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

b1=Button(topFrame,text="Button 1",fg="red")
b2=Button(topFrame,text="Button 2",fg="blue")
b3=Button(topFrame,text="Button 3",fg="green")
b4=Button(bottomFrame,text="Button 4",fg="purple")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=BOTTOM)

root.mainloop()
