# Smallest window containing 0, 1 and 2
# EasyAccuracy: 49.73%
# Given a string S consisting of the characters 0, 1 and 2.
# Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. 
# If no such substring exists, then return -1.

from collections import defaultdict

class Solution:
    def smallestSubstring(self, S):
        a = defaultdict(int)
        
        k = 0
        ans = float('inf')
        for i, j in enumerate(S):
            a[j] += 1
            while len(a) >= 3:
                ans = min(ans, i - k + 1)
                a[S[k]] -= 1
                if a[S[k]] == 0:
                    a.pop(S[k])
                k += 1

        return -1 if ans == float('inf') else ans

