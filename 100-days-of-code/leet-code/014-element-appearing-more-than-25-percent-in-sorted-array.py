# 1287. Element Appearing More Than 25% In Sorted Array
# Easy

# Given an integer array sorted in non-decreasing order, 
# there is exactly one integer in the array that occurs more than 25% of the time, return that integer.


# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
#         return collections.Counter(arr).most_common(1)[0][0]   
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        arr.append(-1)
        curr_counter = 0
        last_v = -1
        for v in arr:
            if v != last_v:
                if curr_counter * 4 > n:
                    return last_v
                curr_counter = 1
                last_v = v
            else:
                curr_counter += 1
        return None
        