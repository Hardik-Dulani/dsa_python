# 1578. Minimum Time to Make Rope Colorful
# Medium

# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. 
# She does not want two consecutive balloons to be of the same color, so she asks Bob for help. 
# Bob can remove some balloons from the rope to make it colorful. 
# You are given a 0-indexed integer array neededTime 
# where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        curr = colors[0]
        val = neededTime[0]
        cost = 0
        for i in range(1,len(colors)):
            if colors[i] == curr:
                cost += min(val,neededTime[i])
                val =  max(val,neededTime[i])
            else:
                curr = colors[i]
                val = neededTime[i]
        return cost