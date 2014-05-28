import sensors
import transportation
import time
import worldPerspective
import random

class Brain:
	sensor = 1
	wheels = 1
	transport = 1
	continueRunning = True
	distThresh = 150 # half a m clear of everything
	def __init__(self):
		sensor = sensors.Sensor()
		transport = transportation.Transportation()
		continueRunning = True
		try:
			while continueRunning:
				# drive forward
				transport.together()
				# check distance
				distanceMeasure = sensor.getUltrasonicReading()
				# if distance < threshold then turn left (30% inc)
				
				while distanceMeasure < self.distThresh:
					transport.turnRight()
					distanceMeasure = sensor.getUltrasonicReading()
				# repeat above until distance > threshold
		except KeyboardInterrupt:
			print "Bye Bye!"
			transport.allOff()


