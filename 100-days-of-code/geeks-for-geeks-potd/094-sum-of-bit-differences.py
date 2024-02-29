# Sum of bit differences
# MediumAccuracy: 60.03%Submissions: 38K+Points: 4
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given an array integers arr[], containing n elements, find the sum of bit differences between all pairs of element in the array. Bit difference of a pair (x, y) is the count of different bits at the same positions in binary representations of x and y.
# For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 respectively and the first and last bits differ between the two numbers.

# Note: (x, y) and (y, x) are considered two separate pairs.


#User function Template for python3
class Solution:

    
    def sumBitDifferences(self,arr, n):
        # code here
        ans = 0
        for i in range(31, -1, -1):
            one = 0
            zero = 0
            for j in range(n):
                bit = 1 << i
                if (arr[j] & bit) > 0:
                    one += 1
                else:
                    zero += 1
            ans += (one * zero) * 2
        return ans

