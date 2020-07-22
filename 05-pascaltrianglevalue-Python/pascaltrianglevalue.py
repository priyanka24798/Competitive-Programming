# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def fun_pascaltrianglevalue(row, col):
    if row >= col:
        num = fact(row)
        
        den = fact(col) * (fact(row -col))
        result = num // den
        return result
    else:
        return 0 


def fact(num):
    res = 1
    for i in range(1,num+1):
        res = res * i
    return res

fun_pascaltrianglevalue(1,1)