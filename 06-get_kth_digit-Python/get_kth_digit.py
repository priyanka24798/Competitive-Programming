# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
    	
		digit = str(digit)
		
		# if digit < 0:
		# 	return 
		
		lst = []
		for i in digit:
			lst.append(i)
			s = (lst[::-1])
			if len(s) >= 3:
				return int(s[k])
			if k >= 3:
				return 0
			
				
    			
		
		return 0
		
    
        
            
    
print(fun_get_kth_digit(789,2))