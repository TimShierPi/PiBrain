import RPi.GPIO as GPIO
import time

class Sensor:

	def lookSee(self):
		try:
			while True:
				GPIO.output(7,1)
				time.sleep(0.0015)
				GPIO.output(7,0)
				time.sleep(2)
		except KeyboardInterrupt:
			GPIO.cleanup()
	
	def __init__(self):
		# init.
		print ("Sensor up!")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7,GPIO.OUT)
		lookSee(self)


