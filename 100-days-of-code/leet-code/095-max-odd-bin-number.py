# 2864. Maximum Odd Binary Number
# Easy
# Topics
# Companies
# Hint
# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be created from the given combination.

# Note that the resulting string can have leading zeros.

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sorted_s = sorted(s, reverse=True)
        for i in range(len(s) - 1, -1, -1):
            if sorted_s[i] == '1':
                sorted_s[i], sorted_s[-1] = sorted_s[-1], sorted_s[i]
                break
        return ''.join(sorted_s)
