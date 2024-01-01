# Array Pair Sum Divisibility Problem
# MediumAccuracy: 27.85%
# Given an array of integers nums and a number k, 
# write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = k * [0]
        for x in arr:
            rem = x % k
            complement = (k - rem) % k
            if counts[complement] >= 1:
                counts[complement] -= 1
            else:
                counts[rem] += 1
        return sum(counts) == 0