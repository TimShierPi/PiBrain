# Transportation handles all controls to the wheel base. 

# Config
FRONTLEFT_GPIO = 14
FRONTRIGHT_GPIO = 11
BACKLEFT_GPIO = 13
BACKRIGHT_GPIO = 12

DEFAULT_DELAY = 0.2 # 200 ms

import RPi.GPIO as GPIO

class Transportation:
	# Base GPIO control methods - TODO
	

	def together(distanceTime=DEFAULT_DELAY, forward=True):
		# move both left and right forward by distanceTime
		print ("Forward! ")
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)
		time.sleep(250)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(15,GPIO.LOW)
		
	
	def turnLeft(distanceTime=DEFAULT_DELAY, counterTurn=True):
		# move left wheels in direction of 'forward'.
		# counter turn makes the other wheels reverse to assist in the turn
		print ("Left! " + distanceTime + " | " + counterTurn)

	def turnRight(distanceTime=DEFAULT_DELAY, counterTurn=True):
		# move right wheels in direction of 'forward'.
		# counter turn makes the other wheels reverse to assist in the turn
		print ("Right! " + distanceTime + " | " + counterTurn)
	
	def __init__(self):
		# init.
		print ("Battleship operational. Wheels engaged.")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(13, GPIO.OUT) # left wheels
		GPIO.setup(15, GPIO.OUT) # right wheels
		