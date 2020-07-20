# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2
def prime(n):
	if n < 0:
		return False
	else:
		for i in range(2, n//2):
			if n % 2 == 0:
				return False
		return True

def palindrome(n):
    	return str(n) == str(n)[::-1]



def fun_nth_palindromic_prime(n):
	num = 1
	while (n > 0):
		
		if prime(n) and palindrome(n):
			n = n -1
		num = num+1

	return a -1
	