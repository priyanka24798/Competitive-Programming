"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	arr = len(array)
	if arr <= 1:
		return array
	else:
		pivot = 0
		for i in range(1, len(array)):
			if array[i] <= array[0]:
				pivot = pivot + 1
				temp = array[i]
				array[i] = array[pivot]
				array[pivot] = temp
		temp = array[0]
		array[0] = array[pivot]
		array[pivot] = temp	

		left = quicksort(array[0: pivot])
		right = quicksort(array[pivot+1: len(array)])	
		sorted_array = left + [array[pivot]] +right

		return sorted_array



	
	# Your code goes here
	pass
