# Write the function inverseLookAndSay(a) that does the inverse of the previous problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
	
	lst = []
	if a == [()]:
		return []
	else:
		for i in a:
			print(i)
			count = i[0]
			num = i[1]
			result = [num]*count
			lst = lst + result
	print(count)	
	print(num)
	return lst

	

inverselookandsay([(2,3),(1,8),(3,-10)])
	# Your code goes here
