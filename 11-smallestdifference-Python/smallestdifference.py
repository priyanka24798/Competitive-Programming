# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	if len(a) == 0:
		return -1
		# return -1
	if len(a) > 1:
		b = sorted(a)
		small = b[0]
		for i in range(len(b)):
			if b[i] < small:
				small = b[i]
		for i in range(1, len(b)):
			if b[i] > small:
				small2 = b[i]
		diff = small2 - small
		return diff
		
		print(diff)
	# Your code goes here
	
print(smallestdifference([19,2,83,6,27]))