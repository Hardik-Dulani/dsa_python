# Max Sum Subarray of size K
# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

#  A subarray is a contiguous part of any given array
# class Solution:   # Not optimized
#     def maximumSumSubarray (self,K,Arr,N):
#         ans = 0
        
#         for i in range(N):
#             curr = 0
#             for j in range(K):
#                 if j+i<len(Arr):
#                     curr+=Arr[j+i]
#             ans = max(curr,ans)
#         return ans