# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	
	b = sorted(a)
	n = len(b)
	
	if n == 0:
		return None
	
	if n % 2 != 0:
		meadian = b[n // 2]
	
	else:
		m1 = b[n // 2]
		m2 = b[(n // 2) - 1]
		meadian = (m1 + m2)/2

	return meadian
