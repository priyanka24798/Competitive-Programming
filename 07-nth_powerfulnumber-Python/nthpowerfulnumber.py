# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

# To find the prime factor :


def ispowerful(n):
    	
	i = 2
	while (n > 1):
		if n % i == 0:	
			if n % (i ** 2) != 0:
				return False
			while  n > 1 and n % 2 == 0:
				n = n // i 
		else:
			i = i + 1
	return True


def nthpowerfulnumber(n):


	list = []
	for i in range (1001):
		if ispowerful(i):
			list.append(i)
	return list[n +1]
