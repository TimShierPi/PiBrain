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
		time.sleep(DEFAULT_DELAY)
		GPIO.output(LEFT_GPIO,GPIO.LOW)
		GPIO.output(RIGHT_GPIO,GPIO.LOW)
		
	
	def turnLeft(distanceTime=DEFAULT_DELAY, counterTurn=True):
		# move left wheels in direction of 'forward'.
		# counter turn makes the other wheels reverse to assist in the turn
		GPIO.output(LEFT_GPIO,GPIO.HIGH)
		time.sleep(DEFAULT_DELAY)
		GPIO.output(RIGHT_GPIO,GPIO.LOW)
		print ("Left!")

	def turnRight(distanceTime=DEFAULT_DELAY, counterTurn=True):
		# move right wheels in direction of 'forward'.
		# counter turn makes the other wheels reverse to assist in the turn
		GPIO.output(LEFT_GPIO,GPIO.HIGH)
		time.sleep(DEFAULT_DELAY)
		GPIO.output(RIGHT_GPIO,GPIO.LOW)
		print ("Right!")
	
	def __init__(self):
		# init.
		print ("Battleship operational. Wheels engaged.")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(LEFT_GPIO, GPIO.OUT) # left wheels
		GPIO.setup(RIGHT_GPIO, GPIO.OUT) # right wheels
		