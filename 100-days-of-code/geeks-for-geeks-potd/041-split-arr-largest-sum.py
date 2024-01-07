# Split Array Largest Sum
# HardAccuracy: 58.9%

# Given an array arr[] of N elements and a number K., 
# split the given array into K subarrays such that the maximum subarray sum achievable out of K subarrays formed is minimum possible. 
# Find that possible subarray sum.


class Solution:
    def splitArray(self, arr, N, K):
        # code here 
        l=max(arr)
        r=sum(arr)
        while(l<=r):
            m=(l+r)//2
            mp=Solution.findsub(arr,m)
            if mp>K:
                l=m+1
            else:
                r=m-1
        return l
        
    def findsub(arr,m):
        k,s=1,0
        for i in arr:
            if s+i<=m:
                s+=i
            else:
                k+=1
                s=i
        return k