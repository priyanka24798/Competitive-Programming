# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a

def ugly(n):
    n = maxDivide(n, 2)
    n = maxDivide(n, 3)
    n = maxDivide(n, 5)
    if n == 1:
        return 1
    else:
        return 0



def fun_nth_uglynumber(n):
    if n == 0:
        return 1
    else:
        count = 1
        i = 1
        while count <= n:
            i = i +1
            if ugly(i):
                count = count + 1
        return i

