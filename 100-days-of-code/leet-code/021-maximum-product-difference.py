# 1913. Maximum Product Difference Between Two Pairs
# Easy

# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z 
# such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

# Return the maximum such product difference.

 
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        

        first_max = 0
        second_max = 0
        first_min = float('inf')
        second_min = float('inf')


        for i in range(len(nums)):
            if nums[i] >= first_max:
                first_max,second_max = nums[i],first_max
            elif nums[i]>second_max:
                second_max = nums[i]
            if nums[i] <= first_min:
                first_min,second_min = nums[i],first_min
            elif nums[i]<second_min:
                second_min = nums[i]


        return (first_max*second_max)-(first_min*second_min)