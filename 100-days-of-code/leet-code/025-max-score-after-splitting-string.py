# 1422. Maximum Score After Splitting a String
# Easy

# Given a string s of zeros and ones, 
# return the maximum score after splitting the string into two non-empty substrings 
# (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = count_zeros_left = 0
        count_ones_right = s.count('1')

        for i in range(len(s) - 1):
            count_zeros_left += s[i] == '0'
            count_ones_right -= s[i] == '1'
            max_score = max(max_score, count_zeros_left + count_ones_right)

        return max_score