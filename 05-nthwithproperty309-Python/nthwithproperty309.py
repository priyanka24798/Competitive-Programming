# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	if n == 0:
		return 309
	x = 310
	k = 1
	while(True):
		result = str(pow(x, 5))
		if ("0","1","2","3","4","5","6","7","8","9" in result):
			if k == n:
				return result
			else:
				k = k + 1
		result = result + 1
