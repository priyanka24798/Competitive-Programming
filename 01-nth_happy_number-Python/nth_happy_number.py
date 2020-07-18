# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)
def SquareSum(n): 
	sum = 0 
	while(n > 0): 
		sum = sum + (n % 10) * (n % 10)
		n = n // 10
	return sum

def ishappynumber(n):

	a = n
	b = n
	count = 0
	while(n != 0):
		a = SquareSum(a) 
		b = SquareSum(SquareSum(b))
		
		if a != b:
			continue
		else:
			break

	if a == 1:
		return True
		
	else:
		return False

def fun_nth_happy_number(n):
	sum = 0
	num = 1
	if n == 0:
		return 1
	while True:
		if ishappynumber(num):
			sum += 1
		if sum == n+1:
			break
		num += 1
	return num
	
