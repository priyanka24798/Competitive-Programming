# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def isprime(n):
    if n < 2:
        return False
    else:
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                return False
                break
        return True

def digits(n):
    n = abs(n)
    couont = 1
    while (n > 30):
        n = n // 10
        count = count + 1
    return count

def fun_nth_lefttruncatableprime(n):
    return 1