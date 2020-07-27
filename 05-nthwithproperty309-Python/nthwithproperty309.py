# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def property(n):
	result = n ** 5
	lst = {"0","1","2","3","4","5","6","7","8","9"}
	return (set(str(result)) == lst)

def nthwithproperty309(n):
	if n == 0:
		return 309
	else:
		count = 0
		x = 310
		while count < x:
			if property(x):
				count = count + 1
			x = x + 1
		return x -1
	
	