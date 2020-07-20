"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    if value not in input_array:
        return -1
    else:
        first = input_array[0]
        last = len(input_array)
        mid = last//2
        while(value != input_array[mid]):
            if value > input_array[mid]:
                first = mid + 1
            else:
                last = mid
            mid = (first + last)//2
        return mid


    # Your code goes here
    pass
