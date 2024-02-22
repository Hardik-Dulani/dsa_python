# Distinct occurrences
# MediumAccuracy: 27.37%
# Given two strings s and t of length n and m respectively. Find the count of distinct occurrences of t in s as a sub-sequence modulo 109 + 7.


class Solution:
    def sequenceCount(self,s, t):
        n = len(s)
        m = len(t)
        mod = 10**9+7
        dp = [[-1 for i in range(m+1)]for j in range(n+1)]

        def solve(s, t, i, j, dp):
            #Base cases
            if j==len(t):
                dp[i][j] = 1
                return 1 
            if i==len(s):
                dp[i][j] = 0
                return 0

            #If the value is already calculated, return it.
            if dp[i][j] != -1:
                return dp[i][j]

            #If the current characters are not equal, move to next character in s.
            if s[i] != t[j]:
                dp[i][j] = solve(s,t,i+1,j,dp)%mod
                return dp[i][j]

            else:
                dp[i][j] = (solve(s,t,i+1,j+1,dp)+solve(s,t,i+1,j,dp)) % mod
                return dp[i][j]

        #Calling the recursive function with initial parameters.
        return solve(s,t,0,0,dp)