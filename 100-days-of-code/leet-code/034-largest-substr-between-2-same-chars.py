# 1624. Largest Substring Between Two Equal Characters
# Easy

# Given a string s, 
# return the length of the longest substring between two equal characters, 
# excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        my_hash = {}
        res = -1 
        for i,c in enumerate(s):
            if c in my_hash:
                res = max(i - my_hash[c] - 1,res)
            else:
                my_hash[c] = i
        return res