#Script used to keep track of important timers in-game:Buff timers, baron/dragon, enemy summoners

#Things to add: Real time timer, reminders, some way to run this as a web app maybe change code to javascript later
import sys
from threading import Timer
print """
Main Menu:
1: Add New Timer
2: List Timers
3: Reset
"""

#Store timers in an array of tuples
timers = []

#Should be quick types = b, d, eb, er, ab, ar
#Automatically erase the entries after the elapsed time has passed
def add(type, currentTime):
	type = type.lower()
	#baron
	if (type == "b"):
		x =("Baron", currentTime + 700)
		Timer(420.0, timers.remove(x)).start()
	#dragon
	elif (type == "d"):
		x = timers.insert(("Dragon", currentTime + 600))
		Timer(360.0, timers.remove(x)).start()
	#enemy blue
	elif (type == "eb"):
		x = timers.insert(("Enemy Blue", currentTime + 500))
		Timer(300.0, timers.remove(x)).start()
	#enemy red
	elif (type == "er"):
		x = timers.insert(("Enemy Red", currentTime + 500))
		Timer(300.0, timers.remove(x)).start()
	#allied red
	elif (type == "ar"):
		x = timers.insert(("Allied Red", currentTime + 500))
		Timer(300.0, timers.remove(x)).start()
	#allied blue
	elif (type == "ab"):
		x = timers.insert(("Allied Blue", currentTime + 500))
		Timer(300.0, timers.remove(x)).start()

	if (len(timers) == 0):
		timers.insert(x)
	else:
		for i in range (0, len(timers)):
			if(timers[i][1] > x(1)):
				timers.insert(i, x)
			elif(i == len(timers)):
				timers.insert(x)

def list():
	#List the timers in order of lowest time
	for i in timers:
		print i

def reset():
	timers = []
