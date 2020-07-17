# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	a = s1.strip()
	b = s2.strip()
	c = s3.strip()
	if b == c:
		print(a)
	
	# result = a+ b + c

	# print(result)
	# return s1

print(fun_replace("helloworld123", "hello", "345"))

