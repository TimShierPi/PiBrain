import sensors
import transportation
import time

class Brain:
	sensor = 1
	wheels = 1
	def __init__(self):
		# init.
		print ("I'm ALIVE!")
		sensor = sensors.Sensor()
		transport = transportation.Transportation()
		transport.together()
		time.sleep(1)
		transport.turnLeft()
		time.sleep(1)
		transport.turnRight()
		print ("And we're done!")
		


