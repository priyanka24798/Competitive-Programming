# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    result = ""
    m = len(s1)
    n = len(s2)
    for i in range (0,m):
        k = 1
        for j in range(0,n):
            while (i + k <= m and j + k <= n) and (s1[ i: i + k] == s2[j: j + k]):
                if (len(result) <= len(s1[i: i + k])):
                    result = s1[i: i + k]
                k = k + 1
                
    return result
 