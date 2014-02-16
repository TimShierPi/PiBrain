import RPi.GPIO as GPIO
import time

class Sensor:
	

	def lookSee(self):
		p = GPIO.PWM(7,50)
		p.start(7.5)
		delayTime =1
		try:
			while True:
				p.ChangeDutyCycle(7.5)
				time.sleep(delayTime)
				p.ChangeDutyCycle(12.5)
				time.sleep(delayTime)
				p.ChangeDutyCycle(7.5)
				time.sleep(delayTime)
				p.ChangeDutyCycle(2.5)
				time.sleep(delayTime)
		except KeyboardInterrupt:
			p.stop()
			GPIO.cleanup()
	
	def __init__(self):
		# init.
		print ("Sensor up!")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7,GPIO.OUT)


