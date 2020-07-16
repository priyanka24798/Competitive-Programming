# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	
	n = str(n)
	
	if len(n) == 1:
		return False

	return True
	# your code goes here
print(hasconsecutivedigits(2))