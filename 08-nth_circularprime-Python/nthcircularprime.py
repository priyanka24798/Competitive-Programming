# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
import math

def isprime(n):
	if n < 2:
		return False
	else:
		for i in range(2, (n//2) + 1):
			if n % i == 0:
				return False
				break
		return True

def iscircular(n):
	count = 0
	temp = n
	while ( temp > 0):
		count = count + 1
		temp = temp // 10
	num = n
	while (isprime(num)):
		rem = num % 10
		div = num / 10
		num = ((math.pow(10, count - 1 ))* rem ) + div
		if num == n:
			return True
	return False

def nthcircularprime(n):
	lst = []
	for i in range(20000):
		if iscircular(i):
			lst.append(i)
	return lst[n]
	# Your code goes here
	pass