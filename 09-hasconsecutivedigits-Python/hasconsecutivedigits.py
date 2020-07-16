# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    
    if n == 0:
        return True
    if  len(str(n)) == 1:
        return False
        

    else:
        # count=0  
        s=abs(n)
        # k=0
        m=[]
        while(s!=0):
                
            k=s%10
            s//=10
            m.append(k)
        for i in m:
            if(m[i]>=m[i+1]):
                return True
            else:
                return False
    
    
    
    # your code goes here
print(hasconsecutivedigits(2))