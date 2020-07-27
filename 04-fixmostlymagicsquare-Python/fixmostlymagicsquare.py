# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	# length = Len(L)
	lst = []
	for i in L:
		j = 0 
		j = j + sum(i)
		lst.append(j)
	if (len(lst) != len(set(lst))):
		diff = max(lst) - min(lst)
		high = max(lst)
		for i in lst:
			if i == high:
				position = lst.index(max(lst))
		result = L[position]
		new_pos = result.index(max(result))
		result[new_pos]= max(result) - diff
		L[position] = result
		return L



