# Search Pattern (Rabin-Karp Algorithm)
# MediumAccuracy: 34.53%Submissions: 47K+Points: 4
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given two strings, one is a text string and other is a pattern string. The task is to print the indexes of all the occurences of pattern string in the text string. For printing, Starting Index of a string should be taken as 1. The strings will only contain lowercase English alphabets ('a' to 'z').


#User function Template for python3

class Solution:
    def search(self, pattern, text):
        # code here
        n=len(text)
        m=len(pattern)
        a=[]
        
        for i in range(n-m+1):
            if text[i:i+m] == pattern:
                a.append(i+1)
        
        return a
