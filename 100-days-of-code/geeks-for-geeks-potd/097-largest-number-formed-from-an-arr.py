# Largest Number formed from an Array
# MediumAccuracy: 37.82%Submissions: 144K+Points: 4
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given an array of strings arr[] of length n representing non-negative integers, arrange them in a manner, such that, 
# after concatanating them in order, it results in the largest possible number. 
# Since the result may be very large, return it as a string.

#User function Template for python3
from functools import cmp_to_key
class Solution:
    def comp(self, a, b): 
        if a + b > b + a: 
            return -1
        return 1

    def printLargest(self, n, arr): 
        # code here
        arr = sorted(arr, key=cmp_to_key(self.comp)) 
        largest_number = "".join(arr) 
        return largest_number

