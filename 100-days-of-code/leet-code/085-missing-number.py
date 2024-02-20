# 268. Missing Number
# Easy
# Topics
# Companies
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)+1):
            try:
                if i!=nums[i]:
                    return i
            except:
                return len(nums)
    