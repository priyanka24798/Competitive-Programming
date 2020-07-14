# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	for i in range(1,f):
		if f % i == 0:
			print(f)
	if f == n:
		return True
    			
	return False # replace with your solution
print(fun_isfactor(-2,4))