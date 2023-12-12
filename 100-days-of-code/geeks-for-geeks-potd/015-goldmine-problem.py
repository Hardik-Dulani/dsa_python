# Gold Mine Problem

# Given a gold mine called M of (n x m) dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner can start from any row in the first column. From a given cell, the miner can move

# to the cell diagonally up towards the right 
# to the right
# to the cell diagonally down towards the right
# Find out maximum amount of gold which he can collect until he can no longer move.

# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        
        dp = [[0] * m for _ in range(n)]

        
        for i in range(n):
            dp[i][m - 1] = M[i][m - 1]

       
        for j in range(m - 2, -1, -1):
            for i in range(n):
                
                right = dp[i][j + 1]
                right_up = dp[i - 1][j + 1] if i > 0 else 0
                right_down = dp[i + 1][j + 1] if i < n - 1 else 0

                dp[i][j] = M[i][j] + max(right, right_up, right_down)

        
        max_gold = 0
        for i in range(n):
            max_gold = max(max_gold, dp[i][0])

        return max_gold