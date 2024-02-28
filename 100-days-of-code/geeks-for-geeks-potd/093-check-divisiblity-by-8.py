# Check if a number is divisible by 8
# EasyAccuracy: 22.22%Submissions: 51K+Points: 2
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given a string representation of a decimal number s, check whether it is divisible by 8


class Solution:
    def DivisibleByEight(self,s):
        
        if int(s[-3:])%8==0:
            return 1
        return -1
