import math
def coordToCartesian(cords):
	print cords
	R = 6371
	alpha = math.radians(cords['lat'])
	beta = math.radians(cords['lng'])
	x = R * math.cos(alpha) * math.cos(beta)
	y = R * math.cos(alpha) * math.sin(beta)
	z = R * math.sin(alpha)
	return [x,y,z]
	
