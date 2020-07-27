# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.




from __future__ import division
import math


def isKaprekarNumber(num):
    if (num == 1): return True
    nsquared = num**2
    count = 1 # count tells us what exponent to use
    right = nsquared%10
    left = nsquared/10
    while (left!=0):
        if (right != 0) and (left+right == num):
            return True
        digit = left%10
        right = right+((10**count)*digit)
        left = left//10
        count += 1
    return False

def fun_nearestkaprekarnumber(n):
    offset = n - int(n)
    upper = int(n)
    lower = int(n)
    while (not isKaprekarNumber(upper)) and (not isKaprekarNumber(lower)):
        upper+=1
        lower-=1
    if isKaprekarNumber(lower):
        if (offset > 0.5):
            upper += 1
        upperDisp = upper - n
        lowerDisp = n - lower
        if (isKaprekarNumber(upper) and (upperDisp < lowerDisp)):
            return upper
        return lower
    return upper

# def fun_nearestkaprekarnumber(n):
#     m = str(n)
#     if len(m) == 2:
#         start = n -10
#         end = n + 10
#     if len(m) == 3:
#         start = n - 100
#         end = n + 100
#     else:
#         start = n - 1500
#         end = n + 1500
#     l = []
#     for i in range(start,end+1):
#         k = float(i)
#         ans = math.log10(k)- math.floor(math.log10(k))
#         if(ans != 0 and iskaprekanumber(i) == True):
#             l.append(i)
#     s =[]
#     for j in l:
#         s.append(abs(j - n))
#     ans = s.index(min(s))
            
#     return l[ans]

print(fun_nearestkaprekarnumber(45))