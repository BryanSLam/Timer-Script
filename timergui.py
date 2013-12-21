#!/usr/bind/python

#Have one root window and multiple frames that you place onto the root window
from Tkinter import *
import tkMessageBox

class Application(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.addLabel = Label(self, text="Add Timer: ")
		self.addLabel.grid(row=0, column=1)

		self.timerEntry = Entry(self)
		self.timerEntry.grid(row=0, column=2)
		self.addButton = Button(self, text="Add", command=self.testEntry)
		self.addButton.grid(row=0, column=3)

	def testEntry(self):
		print self.timerEntry.get()

app = Application()
app.mainloop()