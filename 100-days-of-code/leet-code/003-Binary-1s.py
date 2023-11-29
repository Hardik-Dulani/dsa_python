# Write a function that takes the binary representation of an unsigned integer 
# and returns the number of '1' bits it has (also known as the Hamming weight).
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n-1)
            ans+=1
        return ans