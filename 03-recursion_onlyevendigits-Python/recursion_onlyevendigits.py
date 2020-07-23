# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l): 
		return []


def resultant(l, n, position, new_lst):
	if (position >= n):
		return new_lst
	new_lst.append(evendigit(l[position]), len(str(l[position])),0,"")
	return resultant(l,n,position +1, new_lst)

def evendigit(s, slen, sposition, new_strlst):
	if 