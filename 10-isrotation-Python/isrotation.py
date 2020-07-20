# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
    	
	x = str(x)
	y = str(y)
	if len(y) != len(x):
		return False
	else:
		z == y[::-1]
		if( z == x):
			return True
		return False
			
		
	# Your code goes here
	pass