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
		z= ""
		z = x + x
		a = ""
		a = x + x[::-1]
		if(z.count(y) > 0) or (a.count(y) > 0):
			return True
		return False
			
		
	# Your code goes here
	pass