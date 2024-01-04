# Find element occuring once when all other are present thrice
# MediumAccuracy: 49.87%
# Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
# Find that element which occurs once.

class Solution:
    def singleElement(self, arr, N):
        from collections import Counter
        element_counts = Counter(arr)
        
        return element_counts.most_common()[-1][0]
        