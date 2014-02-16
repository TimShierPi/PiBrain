import brains
import sensors
import curses


class Woof:
	brain = 1
	
	def __init__(self):
		# init.
		print ("W00f!")
		brain = brains.Brain()
		


		

robot = Woof()


#init the curses screen
stdscr = curses.initscr()
#use cbreak to not require a return key press
curses.cbreak()
print "press q to quit"
quit=False
# loop
while quit !=True:
	c = stdscr.getch()
	print curses.keyname(c),
	if curses.keyname(c)=="q" :
		quit=True
	elif curses.keyname(c)=="i":
		print "forward button!"
		robot.brain.transport.together()
	elif curses.keyname(c)=="j":
		print "turn left!"
		robot.brain.transport.turnLeft()
	elif curses.keyname(c)=="l":
		print "turn right!"
		robot.brain.transport.turnRight()
		

