#!/usr/bind/python

#Have one root window and multiple frames that you place onto the root window
from Tkinter import *
import tkMessageBox

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class Application(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.addLabel = Label(self, text="Add Timer: ")
		self.addLabel.grid(row=0, column=1)

		self.timerEntry = Entry(self)
		self.timerEntry.grid(row=0, column=2)
		self.addButton = Button(self, text="Add", command=self.testEntry)
		self.addButton.grid(row=0, column=3)

	#format = type currentTime
	def testEntry(self):
		n = self.timerEntry.get().split(' ')
		if(n[0] != 'b' and n[0] != 'd' and n[0] != 'eb' and n[0] != 'er'
			and n[0] != 'ar' and n[0] != 'ab'):
			tkMessageBox.showinfo("Invalid type", "TYPE WRONG NERD")
		elif(is_number(n[1]) == False):
			tkMessageBox.showinfo("Invalid time", "TIME WRONG TRY AGAIN NERD")
		else:
			self.timerEntry.delete(0, END)

app = Application()
app.mainloop()