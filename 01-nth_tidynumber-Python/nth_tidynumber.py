# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def istidy(n):
    pre = 10
    while(n):
        r = n % 10
        n = n //10
        if r > pre:
            return False
        pre = r
    return True

def fun_nth_tidynumber(n):
    if n == 0:
        return 1
    else:
        lst = []
        for i in range(5000):
            if istidy(i):
                lst.append(i)
        return lst[n + 1]

    return 0