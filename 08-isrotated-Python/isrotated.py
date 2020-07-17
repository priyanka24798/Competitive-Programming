# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
    
	a = len(str1)
	if str1 == str2:
		return False
	
	if a != len(str2):
		return False
	for i in range(a):
		str1 = str1[:1] +str1[0]
		if str1 == str2:
			return True
	
	return False
	#Your code goes here
print(isrotated("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ACDEFGHIJKLMNOPQRSTUVWXYZB"))
