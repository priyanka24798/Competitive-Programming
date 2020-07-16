# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	nstr = str(n)
	dstr = str(d)
	lst = []
	for i in nstr:
		lst.append(i)
	if k >= len(lst):

		s = lst[::-1]
		s.append(dstr)
		r = s[::-1]
	else:
		
        
    
		s = lst[::-1]
		if s[-1] == '-':
			s[k] =  dstr
			s.append('-')
			r = s[::-1]
		else:
			s[k] = dstr
			r = s[::-1]
	
	result = ''.join(r)
	return int(result)
    		
		

