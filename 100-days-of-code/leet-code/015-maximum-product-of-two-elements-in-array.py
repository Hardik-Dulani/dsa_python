# 1464. Maximum Product of Two Elements in an Array
# Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
# you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

# UnOptimized
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
        
#         a = max(nums)
#         nums.remove(a)
#         b = max(nums)
#         return (a-1)*(b-1)


# Optimized
class Solution: 
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for i in range(len(nums)):
            
            if nums[i] >= first:
                first,second = nums[i],first
            elif nums[i]>second:
                second = nums[i]
        return (first-1)*(second-1)
        