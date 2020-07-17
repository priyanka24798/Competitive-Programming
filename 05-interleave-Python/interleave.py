# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



# def fun_interleave(s1,s2):
	# n = len(s1)
	# m = len(s2)
	# if m < n:
	# 	length = n
	# else:
	# 	length = m
	# result = ""
	# for i in range(0,length):
	# 	result += s1[i] + s2[i]
	# if m < n:
	# 	result += s2[length:n]
	# else:
	# 	result += s1[length:m]



	# return result
def fun_interleave(s1,s2):
	if len(s1) < len(s2):
		nu = len(s1)
	else:
		nu = len(s2)
		result = ""
		for i in range(0,nu):
			result += s1[i] + s2[i]
			if len(s1) < len(s2):
				result += s2[nu:len(s2)]
			else:
				result += s1[nu:len(s1)]


	# print(sr)
	return result