# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isprime(n):
	if n <= 1:
		return False
	else:
		for i in range(2, (n//2) +1):
			if (n % i) == 0:
				return False
		return True

def isadd(n):
	# sum = 0:
	n = list(str(n))
	n = list(map(int, n))
	return isprime(sum(n))

 


def fun_nth_additive_prime(n):
	N = 1
	while n >= 0 :
		if isprime(N) and isadd(N):
			n = n-1
		N = N + 1
	return N -1
		
