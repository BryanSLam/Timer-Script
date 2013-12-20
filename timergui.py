#!/usr/bind/python

#Have one root window and multiple frames that you place onto the root window
from Tkinter import *
import tkMessageBox

root = Tk()


addTimerEntry = Entry(root).grid(row=0, column=2)

def entryTest():
	print "wert"


addLabel = Label(root, text="Add Timer:").grid(row=0, column = 1, sticky=W)
addButton = Button(root, text="Add",command=entryTest)
addButton.grid(row = 0, column=3)
resetButton = Button(root, text="Reset").grid(column = 3)
helpButton = Button(root, text="Help").grid(column = 3)

#root.geometry('450x400')
root.title("Buff Timer")
root.mainloop()
