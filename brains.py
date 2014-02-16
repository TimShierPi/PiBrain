import sensors
import transportation
import time
import worldPerspective

class Brain:
	sensor = 1
	wheels = 1
	transport = 1
	def __init__(self):
		# init.
		print ("I'm ALIVE!")
		sensor = sensors.Sensor()
		worldView = worldPerspective.World()
		transport = transportation.Transportation()
		for x in range(0, 1):
			transport.together()
			time.sleep(1)
			transport.turnLeft()
			time.sleep(1)
			transport.turnRight()
			sensor.lookSee()
			print ("And we're done!")
		


