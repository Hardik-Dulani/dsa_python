# Reach the Nth point

# There are N points on the road, you can step ahead by 1 or 2 . 
# If you start from a point 0, and can only move from point i to point i+1 after taking a step of length one, 
# find the number of ways you can reach at point N. 
# class Solution:
# 	def nthPoint(self,n):
# 		dp = [0]*(n+1);
# 		if n<=2:
# 		    return n
#           mod = int(1e9 + 7)
#         for i in range(n+1):
#             if i<=2:
#                 dp[i] = i
#             else:
#                 dp[i] = dp[i-2]+dp[i-1]
#                 dp[i]%=mod
#         return dp[n]
