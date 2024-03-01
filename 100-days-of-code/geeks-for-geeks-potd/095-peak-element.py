# Peak element
# MediumAccuracy: 38.86%Submissions: 403K+Points: 4
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

# Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.
class Solution:   
    def findPeakUtil(self,arr,low,high,n):

        mid=(low+high)//2
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid] ):
            return mid
        elif (mid>0 and arr[mid-1]>arr[mid]):
            return self.findPeakUtil(arr,low,mid-1,n)
        else :
            return self.findPeakUtil(arr,mid+1,high,n)
    def peakElement(self,arr, n):
        return self.findPeakUtil(arr,0,n-1,n)