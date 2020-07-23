# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
from functools import reduce
def longestdigitrun(n):
# 	a = str(n)
# 	b = set(a)
# 	print(b)
# longestdigitrun(117773732)
	try:
		a = str(abs(n))
		return int(reduce(lambda x,y: x if a.count(x) > a.count(y) else y,set(a)))
	except:
		return 1
print (longestdigitrun(11777332))