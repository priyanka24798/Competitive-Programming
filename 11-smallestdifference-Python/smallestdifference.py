# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If  lthe list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.
import math
import os
import random
import re
import sys
def smallestdifference(a):
	if len(a) == 0:
		return None
	else:
		lst = []
		b = sorted(a)
		for i in range(len(b)-1):
			lst.append(abs(b[i]-b[i+1]))
		return min(lst)
	
	
print(smallestdifference([-59,-36,-13,1,-53,-92,-2,-96,-54,75]))