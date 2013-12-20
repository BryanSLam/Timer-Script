#!/usr/bind/python

#Have one root window and multiple frames that you place onto the root window
from Tkinter import *

root = Tk()
#root.geometry('450x400')
root.title("Buff Timer")

addButton = Button(root, text="Add Timer").grid(column=1)
resetButton = Button(root, text="Reset").grid(column = 1)
helpButton = Button(root, text="Help").grid(column = 1)


root.mainloop()