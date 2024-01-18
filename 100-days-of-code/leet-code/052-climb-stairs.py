# 70. Climbing Stairs
# Solved
# Easy

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0 
        b = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        for i in range(2,n+2):
            c = a+b
            a = b
            b = c
        return c