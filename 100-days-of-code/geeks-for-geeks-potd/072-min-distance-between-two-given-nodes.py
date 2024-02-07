# Min distance between two given nodes of a Binary Tree
# MediumAccuracy: 39.13%
# Given a binary tree with n nodes and two node values, a and b, 
# your task is to find the minimum distance between them. 
# The given two nodes are guaranteed to be in the binary tree and 
# all node values are unique.



class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        result = ''
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * -freq
        return result

