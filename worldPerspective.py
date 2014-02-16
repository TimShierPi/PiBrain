class World:

	WORLDWIDTH = 100
	WORLDHEIGHT = 100
	
	worldMap = [[0 for x in xrange(WORLDWIDTH)] for x in xrange(WORLDHEIGHT)]
	
	def __init__(self):
		# init.
		print ("How's the world look?")