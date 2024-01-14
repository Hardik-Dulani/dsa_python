# Find duplicate rows in a binary matrix
# MediumAccuracy: 60.19%
# Given a boolean matrix of size RxC where each cell contains either 0 or 1, 
# find the row numbers (0-based) of row which already exists or are repeated.


class Solution:
    def repeatedRows(self, arr, m ,n):
        visited = []
        ans = []
        for i in range(len(arr)):
            if arr[i] in visited:
                ans.append(i)
            else:
                visited.append(arr[i])
        return ans
