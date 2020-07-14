# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	result = 0
	n = street // 8
	
	# if street == 0:
	# 	return 0
	
	if n == 0:
		if (street % 8) <= 4:
    			
			result += n*8
		else:
			result += (n+1)*8	

	

	if n > 0:
		if (street % 8) <= 4:   			
			result += n*8
		else:
			result += (n+1)*8
	return result 
		
	
			
    		
		
				
			
	
print(fun_nearestbusstop(16))
