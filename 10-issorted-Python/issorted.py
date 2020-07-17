# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	n = len(a)
	b = sorted(a)
	if n == 0 or n == 1:
		return True
	
	for i in range(1, n):
		
		
		if(a[i - 1] > a[i]):
			return False
		
	return True
	
	

	# your code goes here
	
print(issorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))