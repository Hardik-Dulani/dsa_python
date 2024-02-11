# 1463. Cherry Pickup II
# Hard
# Topics
# Companies
# Hint
# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid


class Solution:
    def __init__(self):
        self.dy = [0, -1, 1]
        self.memo = [[[-1] * 71 for _ in range(71)] for _ in range(71)]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for arr2D in self.memo:
            for arr1D in arr2D:
                for i in range(len(arr1D)):
                    arr1D[i] = -1
        return self.dfs(grid, 0, 0, n - 1, m, n)

    def dfs(self, grid, i, c1, c2, m, n):
        if i == m:
            return 0
        if c1 < 0 or c2 < 0 or c1 >= n or c2 >= n:
            return float('-inf')
        if self.memo[i][c1][c2] != -1:
            return self.memo[i][c1][c2]

        ans = 0
        for k in range(3):
            for r in range(3):
                ans = max(ans, self.dfs(grid, i + 1, c1 + self.dy[k], c2 + self.dy[r], m, n))

        ans += grid[i][c1] if c1 == c2 else grid[i][c1] + grid[i][c2]
        self.memo[i][c1][c2] = ans
        return ans

