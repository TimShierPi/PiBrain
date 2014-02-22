import sensors
import transportation
import time
import worldPerspective
import random

class Brain:
	sensor = 1
	wheels = 1
	transport = 1
	distThresh = 350 # half a m clear of everything
	def __init__(self):
		sensor = sensors.Sensor()
		transport = transportation.Transportation()
		while True:
			# drive forward
			transport.together()
			# check distance
			distanceMeasure = sensor.getUltrasonicReading()
			print distanceMeasure
			# if distance < threshold then turn left (30% inc)
			
			while distanceMeasure < self.distThresh:
				if random.random()>0.5:
					transport.turnLeft()
				else:
					transport.turnRight()
				distanceMeasure = sensor.getUltrasonicReading()
				print "In the loop"
				print distanceMeasure
				time.sleep(1.5)
			# repeat above until distance > threshold
			time.sleep(1)
		


