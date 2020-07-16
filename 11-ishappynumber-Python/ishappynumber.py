# ishappynumber(n) [10 pts]
# A happy number is a number defined by the following process: Starting with any positive integer, replace the 
# number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will 
# stay ), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 
# are happy numbers.

# Write the function ishappynumber(n) which takes a possibly-negative integer and returns True if it is happy and 
# False otherwise. Note that all numbers less than 1 are not happy. Here are some test assertions for you:
# assert(ishappynumber(-7) == False)
# assert(ishappynumber(1) == True)
# assert(ishappynumber(2) == False)
# assert(ishappynumber(97) == True)
# assert(ishappynumber(98) == False)
# assert(ishappynumber(404) == True)
# assert(ishappynumber(405) == False)
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num = 82;    
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);    
     
#Happy number always ends with 1    
if(result == 1):    
    print("True")
#Unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print("False")
# def happynumbersum(n):
#     # your code goes here
#     rem = sum = 0
#     while(n):
#         n = abs(n)
#         rem = n%10
#         sum = sum + (rem * rem)
#         n = n//10
#     return sum

# def ishappynumber(n):
#     x = str(happynumbersum(n))
#     l=[]
#     for i in range(len(x)):
#         l.append(x[i])
#     res = 0
#     for i in l:
#         res = res + int(i)*int(i)
        
#     a = str(res)
#     if res == 1:
#         # print(res)
        
#         return True
#     elif len(a) == 1:
#         # print(res)
#         return False
#     else:
#         # print(res)
#         happynumbersum(res)
        
    


# ishappynumber(97)