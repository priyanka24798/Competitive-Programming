# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = {}
	for char in s:
		if char not in d:
			d[char] = s.count(char)
	f = sorted(d.values(), reverse= True)
	val = f[n-1]
	for item in d:
		if d[item] == val:
			result = item
			break
	return result


