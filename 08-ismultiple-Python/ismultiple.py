# Write the function isMultiple that takes two int values m and n 
# and returns True if m is a multiple of n and False otherwise. 
# Note that 0 is a multiple of every integer including itself. 
# Also, you should make constructive use of the isFactor function you just wrote above.



def fun_ismultiple(m, n):
	try:
		if m == 0 and n == 0:
			return True
		elif m != 0 and m%n == 0:
			return True
		elif m!= 0 and n == 0:
			return False
		elif m == 0 and n!= 0:
			return True
	except:
		return False
	return False
				
	# replace with your solution
print(fun_ismultiple(0,6))