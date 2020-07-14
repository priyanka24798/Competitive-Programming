# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	y = (x)
	try:
	
		if y > 0 and y %2 == 0:
			return True
		elif type(y) == str:
			return False

		return False
	except:
		return False
		

	
	

	# your code goes here
	
print(isevenpositiveint((12,)))