# Transportation handles all controls to the wheel base. 

# Config
LEFT_GPIO = 13
RIGHT_GPIO = 15


DEFAULT_DELAY = 0.2 # 200 ms

import RPi.GPIO as GPIO
import time

class Transportation:
	# Base GPIO control methods - TODO
	

	def together(distanceTime=DEFAULT_DELAY, forward=True):
		# move both left and right forward by distanceTime
		print ("Forward! ")
		GPIO.output(LEFT_GPIO,GPIO.HIGH)
		GPIO.output(RIGHT_GPIO,GPIO.HIGH)
		time.sleep(250)
		GPIO.output(LEFT_GPIO,GPIO.LOW)
		GPIO.output(RIGHT_GPIO,GPIO.LOW)
		
	
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
		