# Number of paths in a matrix with k coins
# MediumAccuracy: 16.96%
# Given a n x n matrix such that each of its cells contains some coins. 
# Count the number of ways to collect exactly k coins while moving from top left corner of the matrix to the bottom right. 
# From a cell (i, j), you can only move to (i+1, j) or (i, j+1).

#User function Template for python3

import sys

sys.setrecursionlimit(10**6)

class Solution:
    # Initializing DP array and 2D array 'a'
    dp = [[[-1] * 101 for _ in range(101)] for _ in range(101)]
    a = [[0] * 101 for _ in range(101)]
    
    def go(self, n, m, k):
        # Base Cases
        if k < 0:
            return 0
        if m < 0 or n < 0:
            return 0
        if n == 0 and m == 0:
            # Return 1 if k matches with last element of 'a'
            self.dp[n][m][k] = 1 if k == self.a[n][m] else 0
            return self.dp[n][m][k]
        
        # If already calculated, return the value
        if self.dp[n][m][k] != -1:
            return self.dp[n][m][k]
            
        # Recursively find the number of paths from left and up direction
        left = self.go(n, m-1, k-self.a[n][m])
        up = self.go(n-1, m, k-self.a[n][m])
        
        # Store the result in DP array
        self.dp[n][m][k] = left + up
        return self.dp[n][m][k]

    def numberOfPath(self, n, k, arr):
        # Copying elements from input array to 'a'
        for i in range(n):
            for j in range(n):
                self.a[i][j] = arr[i][j]
        
        # Initializing DP array with -1 for the new case
        for i in range(n):
            for j in range(n):
                for l in range(k+1):
                    self.dp[i][j][l] = -1
        
        # Call the recursive function
        self.go(n-1, n-1, k)
        
        # Return the result
        return self.dp[n-1][n-1][k]


