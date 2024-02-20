# 231. Power of Two
# Easy
# Topics
# Companies
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.


class Solution(object):
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)