# Maximum Index
# MediumAccuracy: 24.5%Submissions: 190K+Points: 4
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given an array a of n positive integers. The task is to find the maximum of j - i subjected to the constraint of a[i] < a[j] and i < j.
#Back-end complete function Template for Python 3

class Solution:
    #Function to find the maximum index difference.
    def maxIndexDiff(self,arr,n):
    
        #Constructing LMin[] such that LMin[i] stores the minimum value 
        #from (arr[0], arr[1], ... arr[i]).
        LMin=[0 for i in range(n)]
        LMin[0]=arr[0]
        for i in range(1,n):
            LMin[i] = min(arr[i],LMin[i-1])
    
        #Constructing RMax[] such that RMax[j] stores the maximum value 
        #from (arr[j], arr[j+1], ..arr[n-1]). 
        RMax=[0 for i in range(n)]
        RMax[n-1]=arr[n-1]
    
        for i in range(n-2,-1,-1):
            RMax[i]=max(arr[i],RMax[i+1])
    
        i,j,maxDiff=0,0,-1
        #Traversing both arrays from left to right to find optimum j-i. 
        #This process is similar to merge() of MergeSort.
        while j<n and i<n:
            if LMin[i]<=RMax[j]:
                #Updating the maximum difference.
                maxDiff=max(maxDiff,j-i)
                j=j+1
            else:
                i=i+1
        #returning the maximum difference.        
        return maxDiff