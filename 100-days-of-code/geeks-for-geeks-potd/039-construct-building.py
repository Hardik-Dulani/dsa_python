# Count possible ways to construct buildings
# MediumAccuracy: 38.53%
# There is a road passing through a city with N plots on both sides of the road. 
# Plots are arranged in a straight line on either side of the road. 
# Determine the total number of ways to construct buildings in these plots, 
# ensuring that no two buildings are adjacent to each other. Specifically, buildings on opposite sides of the road cannot be adjacent.


class Solution:
    def TotalWays(self, n):
        first = 1
        second = 1
        for i in range(1,n+1):
            res = fi+se
            first = se
            second = res%(10**9 + 7)
            
        return (res**2)%(10**9 + 7)
