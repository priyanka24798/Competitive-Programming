# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def longestdigitrun(n):
	try:
		a = str(abs(n))
		result = {}
		for i in a:
			if i in result:
				result[i] += 1
			else:
				result[i] = 1
		longest = min(result, key = result.get)
		# print(str(longest))
		return int(longest)
	except:
		return 1
	# print(a)

print (longestdigitrun(-677886))