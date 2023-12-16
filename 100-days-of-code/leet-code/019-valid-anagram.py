# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= sorted(s)
        t=sorted(t)
        return s==t
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i in s:
            if i in hash1:
                hash1[i]+=1
            else:
                hash1[i] = 1
        for j in t:
            if j in hash2:
                hash2[j]+=1
            else:
                hash2[j] = 1
        
        
        return hash1==hash2