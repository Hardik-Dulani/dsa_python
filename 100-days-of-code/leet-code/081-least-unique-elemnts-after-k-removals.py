# 1481. Least Number of Unique Integers after K Removals
# Medium
# Topics
# Companies
# Hint
# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        mp = {}
        for x in arr:
            mp[x] = mp.get(x, 0) + 1

        elements = sorted(mp.items(), key=lambda x: x[1])

        for key, value in elements:
            if value <= k:
                k -= value
                del mp[key]
            else:
                break
        return len(mp)