# Game with String
# MediumAccuracy: 53.96%
# Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. The value of a string is defined as the sum of squares of the count of each distinct character present in the string. 


import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        counter = Counter(s)
        counts = [-v for v in counter.values()]
        heapq.heapify(counts)
        
        while k > 0:
            max_count = heapq.heappop(counts)
            heapq.heappush(counts, max_count+1)
            k -= 1
        
        return sum(i**2 for i in counts)
            
            
