import sensors
import transportation

class Brain:
	sensor = 1
	wheels = 1
	def __init__(self):
		# init.
		print ("I'm ALIVE!")
		sensor = sensors.Sensor()
		transport = transportation.Transportation()
		transport.together()
		transport.turnLeft()
		transport.turnRight()
		


