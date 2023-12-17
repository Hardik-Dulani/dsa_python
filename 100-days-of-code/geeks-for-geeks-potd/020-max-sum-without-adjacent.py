
# Max Sum without Adjacents
# EasyAccuracy: 47.25%

# Given an array Arr of size N containing positive integers. 
# Find the maximum sum of a any possible subsequence such that no two numbers in the subsequence should be adjacent in Arr.


class Solution:
    
    def findMaxSum(self,arr, n):
        if n == 1:
            return arr[0]
        if n == 2:
            return arr[0] if arr[0] > arr[1] else arr[1]
        p, q = arr[0], max(arr[0], arr[1])
        i = 2
        
        while i < n:
            p, q = q, max(q, arr[i] + p)
            i += 1
        return q