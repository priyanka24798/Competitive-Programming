# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

import math

def ispronic(n):
	x = int(math.sqrt(n))
	if (x*(x + 1)== n):
		return True
	else:
		return False
    		

def nthpronicnumber(n):
	count = 1
	i = 1
	while( count < n):
		if ispronic(n):
			count = count +1
		i = i + 1
	return  i - 1
