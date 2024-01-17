# 1207. Unique Number of Occurrences
# Solved
# Easy

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ref = sorted(Counter(arr).values())
        prev = 0
        for i in ref:
            if i == prev:
                return False
            prev = i
        return True