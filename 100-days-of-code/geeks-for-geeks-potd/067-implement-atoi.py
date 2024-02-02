# Implement Atoi
# MediumAccuracy: 32.58%
# Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions.
# If the conversion is not feasible, the function should return -1.

# Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.


#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        s = s.upper()
        if s[-1]=='-':
            return -1
        ans = 0
        for i in range(65,90+1):
            if chr(i) in s:
                ans=True
        
        ff = s
        if ans!=True:
            ff=int(s)
        return -1 if ans==True else ff
