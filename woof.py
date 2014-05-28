import brains
import sensors
import curses


class Woof:
	
	def __init__(self):
		# init.
		print ("W00f!")
		brain = brains.Brain()
	def starter(self):
		brain = brains.Brain()
	
	def stopper(self):
		print "Computer says stop"
		brain.continueRunning = False


		

robot = Woof()	

