# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	count = 0
	result = tuple()
	lst =[]
	if a == []:
		return lst
	else:
		for i in range(0,len(a)):
			if i==0:
				count = 1
				for j in range (i +1, len(a)):
					if a[i] == a[j]:
						count += 1
					else:
						break
						count = 1
				result = count,a[i]
				lst.append(result)
			else:
				if a[i] == a[i -1]:
					continue
				else:
					count =0
					for j in range (i, len(a)):
						if a[i] == a[j]:
							count = count + 1
					result = count,a[i]
					lst.append(result)
		return lst
	# Your code goes here
	pass

	lookandsay([3,3,8,-10,-10,-10])