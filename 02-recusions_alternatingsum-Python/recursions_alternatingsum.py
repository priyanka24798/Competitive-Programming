# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l): 
	if (len(l) == 0):
		return 0

	return alternating(l, position, result)

def alternating(l, position, result):
	result = 0
	if position % 2 == 0:
		result = result + l[position]
	else:
		result = result - l[position]
	position += 1
	return alternating(l, position, result)