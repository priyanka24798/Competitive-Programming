# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	if n == 0:
		return 0
	if n > 0:
		a = str(n)
		lst =[]
		count = 0
		for i in a:
			lst.append(i)
			s = list(map(int,lst))
		max = 0
		res = s[0] 
		for i in s: 
			freq = s.count(i)
			if freq > max: 
				max = freq 
				res = i 
		
		return res
mostfrequentdigit(2342)