# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	a = distance(x1,y1,x2,y2)
	b = distance(x2,y2,x3,y3)
	c = distance(x3,y3,x1,y1)
	# rt = a**2 + b**2
	# l = c**2
	if a + b ==  c:
		return True
	if b + c == a:
		return True
	if c + a == b:
		return True
	else:
		return False
	# your code goes here
	

def distance(x1,y1,x2,y2):
	dist = ((x2 - x1)**2 + (y2 - y1)**2)
	return dist

print(isrighttriangle(6, 1, 0, 4, -1, -7))