# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


# import math

# def fun_nth_kaprekarnumber(n):
#     if(n == 0):
#         return 1
#     else:

#         # # a = n ** 2
#         # count = 0
        
#         # result = 1
#         # while (count < n):
            
#         #     result = result +1
#         #     a = int(math.pow(result, 2))
#         #     temp = a
#         #     multiplier = 0
#         #     while (temp > 0):
#         #         multiplier = multiplier +1
#         #         temp = temp // 10
#         #     for i in range (multiplier):
#         #         if (temp % ((10) ** i) != 0):
#         #             if result == ((temp // ((10)**i)) + (temp % ((10) ** i))):
#         #                 count = count +1
#         #                 break
#         # return result


# print(fun_nth_kaprekarnumber(5))
import math
def fun_nth_kaprekarnumber(n):
    if(n==0):
        return 1
    c=0
    i=1
    while(c<n):
        i=i+1  
        q=int(math.pow(i,2))
        m=0
        f=q
        while(f>0):
            m=m+1
            f=f//10
        for j in range(m):
            t=q//((10)**j)
            p=q%((10)**j)
            if(p!=0) :
                if(i==t+p):

                    c=c+1
                    break
                
    return i

