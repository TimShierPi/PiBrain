# Transportation handles all controls to the wheel base.

# Config
LEFT_GPIO_1 = 15
LEFT_GPIO_2 = 13
RIGHT_GPIO_1 = 16
RIGHT_GPIO_2 = 12


DEFAULT_DELAY = 0.2 # 100 ms

import RPi.GPIO as GPIO
import time

class Transportation:
	# Base GPIO control methods - TODO
	

	def together(distanceTime=DEFAULT_DELAY, forward=True):
		# move both left and right forward by distanceTime
		GPIO.output(LEFT_GPIO_1,GPIO.HIGH)
		GPIO.output(LEFT_GPIO_2,GPIO.LOW)
		GPIO.output(RIGHT_GPIO_1,GPIO.HIGH)
		GPIO.output(RIGHT_GPIO_2,GPIO.LOW)
		time.sleep(DEFAULT_DELAY)
		GPIO.output(LEFT_GPIO_1,GPIO.LOW)
		GPIO.output(RIGHT_GPIO_1,GPIO.LOW)
		GPIO.output(LEFT_GPIO_2,GPIO.LOW)
		GPIO.output(RIGHT_GPIO_2,GPIO.LOW)

	def backwards(self):
		GPIO.output(LEFT_GPIO_1, GPIO.LOW)
		GPIO.output(LEFT_GPIO_2,GPIO.HIGH)
		GPIO.output(RIGHT_GPIO_1, GPIO.LOW)
		GPIO.output(RIGHT_GPIO_2, GPIO.HIGH)
		time.sleep(DEFAULT_DELAY)
		GPIO.output(LEFT_GPIO_1, GPIO.LOW)
		GPIO.output(LEFT_GPIO_2, GPIO.LOW)
		GPIO.output(RIGHT_GPIO_1, GPIO.LOW)
		GPIO.output(RIGHT_GPIO_2, GPIO.LOW)
		
	
	# TODO - make it work with the web server. Future Tim.
	def togetherOn(self):
		GPIO.output(LEFT_GPIO_1, GPIO.HIGH)
		GPIO.output(RIGHT_GPIO_1, GPIO.HIGH)
	def togetherOff(self):
		GPIO.output(LEFT_GPIO_1, GPIO.LOW)
		GPIO.output(RIGHT_GPIO_1, GPIO.LOW)
	def leftOn(self):
		GPIO.output(LEFT_GPIO_1,GPIO.HIGH)

	def leftOff(self):
		GPIO.output(LEFT_GPIO_1,GPIO.LOW)

	def rightOn(self):
		GPIO.output(RIGHT_GPIO_1, GPIO.HIGH)

	def rightOff(self):
		GPIO.output(RIGHT_GPIO_1, GPIO.LOW)
	
	def allOff(self):
		GPIO.output(RIGHT_GPIO_1, GPIO.LOW)
		GPIO.output(RIGHT_GPIO_2, GPIO.LOW)
		GPIO.output(LEFT_GPIO_1, GPIO.LOW)
		GPIO.output(LEFT_GPIO_2, GPIO.LOW)
		
	
	def turnRight(distanceTime=DEFAULT_DELAY, counterTurn=True):
		# move right wheels in direction of 'forward'.
		# counter turn makes the other wheels reverse to assist in the turn
		GPIO.output(RIGHT_GPIO_1,GPIO.HIGH)
		GPIO.output(RIGHT_GPIO_2,GPIO.LOW)
		if counterTurn:
			GPIO.output(LEFT_GPIO_1,GPIO.LOW)
			GPIO.output(LEFT_GPIO_2,GPIO.HIGH)
		time.sleep(DEFAULT_DELAY*2)
		GPIO.output(RIGHT_GPIO_1,GPIO.LOW)
		GPIO.output(RIGHT_GPIO_2,GPIO.LOW)
		
		if counterTurn:
			GPIO.output(LEFT_GPIO_1,GPIO.LOW)
			GPIO.output(LEFT_GPIO_2,GPIO.LOW)

	def turnLeft(distanceTime=DEFAULT_DELAY, counterTurn=True):
		# move right wheels in direction of 'forward'.
		# counter turn makes the other wheels reverse to assist in the turn
		GPIO.output(LEFT_GPIO_1,GPIO.HIGH)
		GPIO.output(LEFT_GPIO_2,GPIO.LOW)
		if counterTurn:
			GPIO.output(RIGHT_GPIO_1,GPIO.LOW)
			GPIO.output(RIGHT_GPIO_2,GPIO.HIGH)
		time.sleep(DEFAULT_DELAY*2)
		GPIO.output(LEFT_GPIO_1,GPIO.LOW)
		GPIO.output(LEFT_GPIO_2,GPIO.LOW)
		if counterTurn:
			GPIO.output(RIGHT_GPIO_1, GPIO.LOW)
			GPIO.output(RIGHT_GPIO_2, GPIO.LOW)
	
	def __init__(self):
		# init.
		print ("Battleship operational. Wheels engaged.")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(LEFT_GPIO_1, GPIO.OUT) # left wheels
		GPIO.setup(RIGHT_GPIO_1, GPIO.OUT) # right wheels
		GPIO.setup(LEFT_GPIO_2, GPIO.OUT)
		GPIO.setup(RIGHT_GPIO_2, GPIO.OUT)
		# run through the boot tests.
		together()
		backwards()
		turnRight(0.5)
		time.sleep(1)
		turnLeft(0.5)
		time.sleep(1)
		allOff()
