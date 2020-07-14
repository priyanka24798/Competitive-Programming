# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	p = 0
	if eggs >= 0:
		carton = eggs/12
		p = p + carton
		r = eggs%12
		if r >= 1:
			p = p +1
			return int(p)
		else:
			return int(p)

	# your code goes here
	
