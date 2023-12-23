# Count More than n/k Occurences

# Given an array arr of size N and an element k. 
# The task is to find the count of elements in the array that appear more than n/k times
#User function Template for python3
from collections import defaultdict

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        ref =  defaultdict(int)
        var = n/k
        ans = 0
        for i in arr:
            ref[i]+=1
        for i,j in ref.items():
            if j>var:
                ans+=1
        return ans
