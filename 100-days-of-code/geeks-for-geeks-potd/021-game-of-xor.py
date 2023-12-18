# Game of XOR
# MediumAccuracy: 50.77%

# Given an array A of size N. 
# The value of an array is denoted by the bit-wise XOR of all elements it contains. 
# Find the bit-wise XOR of the values of all subarrays of A.

#User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        ans = 0
        if N%2 == 0:
            return ans
        for i in range(0,N,2):
            ans^=A[i]
        return ans