# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	n = int(n)
	if n  <= 0 or n < 1:
		return None
	if n == 1:
		return [1]
	else:
		power3(n, 1, [])
	
def power3(n, N, l):
	if N > n:
		return l
	if (1162261467 % N == 0):
		l.append(N)
	return (n, N+1, l)