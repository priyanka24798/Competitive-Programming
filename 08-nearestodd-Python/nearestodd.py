# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

# import numpy as np

def fun_nearestodd(n):
	try:
		f = int(n)
		
		if f % 2 == 0 and f != n:
			return f +1
		if f % 2 == 0 and f == n:
			return f -1
		
			
		else:
			return f
	except:
		return int(n)
fun_nearestodd(31.6)	
    	
	
	

