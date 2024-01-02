# Largest Sum Subarray of Size at least K


# Given an array a of length n and a number k, find the largest sum of the subarray containing at least k numbers. 
# It is guaranteed that the size of array is at-least k.

class Solution():
    def maxSumWithK(self, a, n, k):
        frontsum = 0
        cursum =0
        j = 0
        for i in range(k):
            cursum += a[i]
        ans = cursum
        for i in range(k,n,1):
            cursum += a[i]
            frontsum += a[j]
            j += 1
            if frontsum < 0:
                cursum -= frontsum
                frontsum = 0
            ans = max(ans,cursum)
        return ans