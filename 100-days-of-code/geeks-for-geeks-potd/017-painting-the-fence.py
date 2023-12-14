# Painting the Fence

# Given a fence with n posts and k colors, 
# find out the number of ways of painting the fence so that not more than two consecutive posts have the same colors. 
# Since the answer can be large return it modulo 10**9 + 7.
class Solution:
    def countWays(self,n,k):
        #code here.

        if n == 1:
            return k
            
        same, diff, mod = 0, k, 10**9 + 7
        for i in range(2, n+1):
            same, diff = diff, ((same + diff) * (k - 1)) % mod
        
        return (same + diff) % mod