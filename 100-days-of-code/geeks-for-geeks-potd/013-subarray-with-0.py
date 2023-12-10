# Subarray with 0 sum

# Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum.
# You just need to return true/false depending upon whether there is a subarray present with 0-sum or not. 
# Printing will be taken care by the driver code.
#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        prefix_sum = 0
        hash_table = set([])
        for i in arr:
            prefix_sum += i
            if prefix_sum == 0:
                return True
            if prefix_sum in hash_table:
                return True
            hash_table.add(prefix_sum)
        return False