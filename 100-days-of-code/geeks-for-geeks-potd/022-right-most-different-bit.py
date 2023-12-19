# Rightmost different bit
# EasyAccuracy: 61.61%


# Given two numbers M and N. 
# The task is to find the position of the rightmost different bit in the binary representation of numbers. 
# If both M and N are the same then return -1 in this case.



class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self, m, n):
        # If both numbers are the same, return -1.
        if m == n:
            return -1
        
        # Find the XOR of the two numbers to get the bits that are different.
        xor_result = m ^ n
        
        # Find the position of the rightmost set bit in the XOR result.
        position = 1
        while xor_result:
            # Check if the current bit is set (i.e., 1).
            if xor_result & 1:
                return position
            # Right shift to move to the next bit position.
            xor_result >>= 1
            position += 1
        
        # If no different bit is found (i.e., both numbers are the same),
        # return -1 as per the problem statement.
        return -1