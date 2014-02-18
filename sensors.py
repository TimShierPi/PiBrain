import RPi.GPIO as GPIO
import time

class Sensor:
	ULTRASONIC_TRIGGER = 16
	ULTRASONIC_ECHO = 18

	def lookSee(self):
		p = GPIO.PWM(7,50)
		p.start(7.5)
		delayTime =1
		try:
			while True:
				p.ChangeDutyCycle(7.5)
				print self.getUltrasonicReading()
				time.sleep(delayTime)
				p.ChangeDutyCycle(12.5)
				print self.getUltrasonicReading()
				time.sleep(delayTime)
				p.ChangeDutyCycle(7.5)
				print self.getUltrasonicReading()
				time.sleep(delayTime)
				p.ChangeDutyCycle(2.5)
				print self.getUltrasonicReading()
				time.sleep(delayTime)
		except KeyboardInterrupt:
			p.stop()
			GPIO.cleanup()
			
	def getUltrasonicReading(self):
		# Send 10us pulse to trigger
		GPIO.output(self.ULTRASONIC_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(self.ULTRASONIC_TRIGGER, False)
		start = time.time()

		while GPIO.input(self.ULTRASONIC_ECHO)==0:
			start = time.time()

		while GPIO.input(self.ULTRASONIC_ECHO)==1:
			stop = time.time()

		# Calculate pulse length
		elapsed = stop-start

		# Distance pulse travelled in that time is time
		# multiplied by the speed of sound (cm/s)
		distance = elapsed * 34300

		return distance
	
	def __init__(self):
		# init.
		print ("Sensor up!")
		GPIO.setmode(GPIO.BOARD)
		# set up servo
		GPIO.setup(7,GPIO.OUT)
		# set up ultrasonic
		ULTRASONIC_TRIGGER = 16
		ULTRASONIC_ECHO = 18
		GPIO.setup(self.ULTRASONIC_TRIGGER,GPIO.OUT)  # Trigger
		GPIO.setup(self.ULTRASONIC_ECHO,GPIO.IN)      # Echo
		GPIO.output(self.ULTRASONIC_TRIGGER, False)


