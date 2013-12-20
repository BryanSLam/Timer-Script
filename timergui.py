#!/usr/bind/python

#Have one root window and multiple frames that you place onto the root window
from Tkinter import *

root = Tk()
root.geometry('450x400')
root.title("Buff Timer")

buttonFrame = Frame(root, width=50, height=400)

addButton = Button(buttonFrame,text="Add Timer").pack(side=RIGHT)
helpButton = Button(buttonFrame,text="Help").pack(side=RIGHT)
resetButton = Button(buttonFrame,text = "Reset").pack(side=RIGHT)

buttonFrame.pack(side=RIGHT)

root.mainloop()