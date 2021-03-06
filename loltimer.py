#Script used to keep track of important timers in-game:Buff timers,
#baron/dragon, enemy summoners

#Things to add: Real time timer, reminders, some way to run this as a web app
#maybe change code to javascript later
import sys
from threading import Timer

################ Helper functions ####################
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def timeConvertor(s):
	#The last two numbers should always be the seconds so 
	#place a colon before the 2nd to last character
	#Strings in python are immutable but they're still
	#an array of characters so just construct a new string from
	#the existing one
	return s[0: len(s)-2] + ":" + s[len(s)-2:len(s)]

##################### Main Area #######################
#Store timers in an array of tuples
timers = []
timerObjects = []

def menu():
	print """
Main Menu:
1: Add New Timer
2: List Timers
3: Reset
4: Help
0: Exit
	"""
	s = ""
	while(s != '1' and s != '2' and s != '3' and s != '0' and s != '4'):
		s = raw_input('>')

		if(s == '1'):
			print "Add a timer"
			#Predefine the variables for error checking
			time = "abc"
			type = "123"
			while(is_number(time) == False):
				time = raw_input('Time: ')
				if(is_number(time) == False):
					print "Enter a correct time"
			while(type != "b" and type != "d" and type != "eb" and type!= "er" 
					and type!= "ab" and type!= "ar"):
				
				type = raw_input('Type: ')
				
				if(type != "b" and type != "d" and type != "eb" and type!= "er" 
					and type!= "ab" and type!= "ar"):
					print "Enter a correct objective"

			add(type, int(time))
		elif(s == '2'):
			list()
		elif(s == '3'):
			reset()
		elif(s == '4'):
			help()
		elif(s == '0'):
			for i in timerObjects:
				i.cancel()
			sys.exit()



#Should be quick types = b, d, eb, er, ab, ar
#Automatically erase the entries after the elapsed time has passed
#New plan, store the information in tuples which will be arranged by lowest 
#time in an array
#Each tuple holds the type of objective, the time it'll respawn, and how much 
#time till it must be removed from the array
def add(type, currentTime):
	type = type.lower()
	#baron
	if (type == "b"):
		x =("Baron", currentTime + 700, 420.0)
	#dragon
	elif (type == "d"):
		x = ("Dragon", currentTime + 600, 360.0)
	#enemy blue
	elif (type == "eb"):
		x = ("Enemy Blue", currentTime + 500, 300.0)
	#enemy red
	elif (type == "er"):
		x = ("Enemy Red", currentTime + 500, 300.0)
	#allied red
	elif (type == "ar"):
		x = ("Allied Red", currentTime + 500, 300.0)
	#allied blue
	elif (type == "ab"):
		x = ("Allied Blue", currentTime + 500, 300.0)
	else:
		print "Type doesn't exist"
		return

	if (len(timers) == 0):
		timers.append(x)

	else:
		for i in range (0, len(timers)):
			if(timers[i][1] > x[1]):
				timers.insert(i, x)
			elif(i == len(timers)-1):
				timers.append(x)
	#Timer will normally evaluate timers.remove and remove before creating the
	#timer object, to remedy this use a lambda function which won't execute
	#because it's annoymous until it's called by the timer object...I think
	t = Timer(x[2], lambda: timers.remove(x))
	t.start()
	timerObjects.append(t)
	print "Added to list will be removed in " + str(x[2]) + " seconds"

def list():
	#List the timers in order of lowest time
	if (len(timers) == 0):
		print "No timers available"
	for i in timers:
		print i[0] +" "+ timeConvertor(str(i[1]))

def reset():
	timers = []

def help():
	print """
	When Adding times make sure the Time input is the current time without the 
	colon : EX: 17:00 -> 1700
	
	For types abbreviate the objective: Enemy Blue -> eb Allied Blue -> ab
	Dragon -> d Baron -> b

	Timers are automatically removed when the objective spawns 

	Reset will clear all timers

	If you enter an invalid timer that raises an exception like entering
	"dragon" when asked for the current time, the script won't exit until 
	all timers have run their course.
	"""
#Start shit up
while(True):
	menu()
