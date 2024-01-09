# Search Pattern (KMP-Algorithm)
# MediumAccuracy: 45.04%
# Given two strings, one is a text string, txt and other is a pattern string, pat. 
# The task is to print the indexes of all the occurences of pattern string in the text string. 
# Use one-based indexing while returing the indices. 
# Note: Return an empty list incase of no occurences of pattern. Driver will print -1 in this case.


class Solution:
    def search(self, pat, txt):
        l = len(pat)
        a = []
        for i in range(len(txt)):
            if txt[i:i+l] == pat:
                a.append(i+1)
        if a!=[]:
            return a
        return [-1]

