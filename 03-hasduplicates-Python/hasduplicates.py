# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	result = []
	for i in range(0, len(L)):
		for j in range(0, len(L[0])):
			if L[i][j] in result:
				return True
			else:
				result.append(L[i][j])
	return False
		