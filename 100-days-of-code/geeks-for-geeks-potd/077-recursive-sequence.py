# Recursive sequence
# EasyAccuracy: 49.57%
# A function F is defined as follows F(n)= (1) +(2*3) + (4*5*6) ... upto n terms 
# (look at the examples for better clarity). Given an integer n, determine the F(n).

# Note: As the answer can be very large, return the answer modulo 109+7.

#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        MOD=10**9+7
        sum_val=0
        add=1
        for i in range(n):
            prd=1
            for j in range(i+1):
                prd=(prd*add) % MOD
                add += 1
            sum_val=(sum_val+prd)%MOD
        return sum_val