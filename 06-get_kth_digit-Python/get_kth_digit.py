# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	a = str(digit)
	c = str(k)
	b = []
	for i in a:
		b.append(i)
		if b[0] == c:
			print(b[0])
	# print(b[0]) 

		
			
	# print(b)
	# if digit <= 0 and k != 0:
	# 	return k
	# return 0
print(fun_get_kth_digit(789, 1))
