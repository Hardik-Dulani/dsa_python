# First element to occur k times
# EasyAccuracy: 37.11%Submissions: 185K+Points: 2
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given an array of n integers. Find the first element that occurs atleast k number of times. If no such element exists in the array, then expect the answer to be -1.

#User function Template for python3
from collections import Counter

class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        mydict = dict()
        for val in a:
            mydict[val] = mydict.get(val, 0) + 1
            if mydict.get(val, 0) >= k:
                return val
        return -1        
    

