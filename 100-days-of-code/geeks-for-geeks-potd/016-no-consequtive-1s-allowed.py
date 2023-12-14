# Given a positive integer N, 
# count all possible distinct binary strings of length N such that there are no consecutive 1’s. 
# Output your answer modulo 109 + 7.

class Solution:

    def countStrings(self,n):
        # code here
        if n==0:
            return 1
        elif n==1:
            return 2
        else:
            dp=[0]*(n+1)
            dp[1]=2
            dp[2]=3
            for i in range(3,n+1):
                dp[i]=(dp[i-1]+dp[i-2])%1000000007
            return dp[n]