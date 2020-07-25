# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.


def isautomorphic(n):
	square = n * n
	while ( n > 0):
		if ( n % 10 != square % 10 ):
			return False
		n = n // 10
		square = square // 10
	return True

def nthautomorphicnumbers(n):
	count = 0
	i = 0
	while count < n:
		if isautomorphic(i):
			count = count + 1
		i = i + 1
	return i-1
	