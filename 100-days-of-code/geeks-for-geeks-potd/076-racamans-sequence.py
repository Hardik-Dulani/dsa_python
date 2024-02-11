# Recamans sequence
# EasyAccuracy: 51.31%
# Given an integer n, return the first n elements of Recaman’s sequence.
# It is a function with domain and co-domain as whole numbers. It is recursively defined as below:
# Specifically, let a(n) denote the (n+1)th term. (0 being the 1st term).
# The rule says:
# a(0) = 0
# a(n) = a(n-1) - n, if a(n-1) - n > 0 and is not included in the sequence previously
#        =  a(n-1) + n otherwise.

#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # code here
        dp=[0 for i in range(n)]
        seen=set(dp)
        for i in range(1,n):
            x=dp[i-1]-i
            if x<0 or x in seen:
                dp[i]=x+i+i
                seen.add(x+i+i)
            else:
                dp[i]=x
                seen.add(x)
        return dp
